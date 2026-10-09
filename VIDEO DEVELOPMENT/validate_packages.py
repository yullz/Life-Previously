"""Read-only structural validation of director development packages.
Run: python "VIDEO DEVELOPMENT/validate_packages.py" --draft
Or:  python "VIDEO DEVELOPMENT/validate_packages.py" --folder "01 - Surviving the Winter of 1709" --draft
Final release: omit --draft. This never performs a historical or media review.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
REQUIRED=["episode.json","START_HERE.md","script.txt","narration.md","claims.md","claims.json","sources.json","research.md","period.txt","scene_plan.json","visual_assets.json","image_prompts.json","director_prompt_plan.json","wardrobe_spec.json","sound_plan.json","pronunciations.json","thumbnail_brief.md","package.md","shorts_plan.json","director_to_claude.json","EXECUTION.md","qa.md","review.json"]

def read(p): return json.loads(p.read_text(encoding="utf-8-sig"))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def validate(folder,draft=False):
    errors=[];warnings=[]
    def need(condition,message):
        if not condition: errors.append(message)
    missing=[f for f in REQUIRED if not (folder/f).is_file()]
    if missing: return {"folder":folder.name,"errors":["Missing: "+", ".join(missing)],"warnings":[]}
    d=read(folder/"episode.json");sp=read(folder/"scene_plan.json");scenes=sp["scenes"]
    claims=read(folder/"claims.json");sources=read(folder/"sources.json");plan=read(folder/"director_prompt_plan.json")
    ss={s["scene_id"]:s for s in scenes};cs={c["id"]:c for c in claims};src={s["id"]:s for s in sources}
    need(len(ss)==len(scenes),"Duplicate scene IDs")
    need(len(cs)==len(claims),"Duplicate claim IDs")
    need(len(src)==len(sources),"Duplicate source IDs")
    words=sum(len(s["narration"].split()) for s in scenes)
    need(1650<=words<=1900,f"Narration outside1650–1900 words: {words}")
    requests=plan["requests"];rs={r["scene_id"]:r for r in requests}
    need(len(rs)==len(requests),"Duplicate image requests")
    graphic_ids={s["scene_id"] for s in scenes if s["asset_type"]=="local_graphic"}
    need(set(rs).isdisjoint(graphic_ids),"Local graphic submitted as paid illustration")
    need(set(ss)==set(rs)|graphic_ids,"Scene assets have omissions/orphans")
    cfg=read(ROOT/"pipeline/config.json");phrases=cfg.get("banned_phrases",[])
    pose_map=read(ROOT/"channel/poses.json");seen=set()
    for s in scenes:
        sid=s["scene_id"];need(bool(s["narration"].strip()),sid+" empty narration")
        need(len(s["narration"].split())<=28,sid+" exceeds28 words")
        need(bool(s["claim_ids"]),sid+" lacks claim/framing mapping")
        for cid in s["claim_ids"]:
            need(cid in cs,sid+" unknown claim "+cid)
            if cid in cs: need(sid in cs[cid]["scene_ids"],sid+" not in reverse claim mapping "+cid)
        for phrase in phrases:
            if re.search(r"(?<!\w)"+re.escape(phrase)+r"(?!\w)",s["narration"],re.I):
                errors.append(sid+" banned phrase: "+phrase)
        p=s.get("parent_scene")
        if p: need(p in seen and p in rs,sid+" invalid/unbuilt parent "+p)
        v=s.get("visitor")
        if v:
            pose=v["pose"];need(pose in pose_map,sid+" unknown pose "+pose)
            need(pose not in ["phone-up","closeup-phone"],sid+" retired phone pose")
            need((ROOT/v["source"]).exists(),sid+" pose source missing")
            need(s["shot_type"]!="object insert" or pose.startswith("closeup-"),sid+" full body on object insert")
            if d.get("pirate_hat"):need(bool(v.get("accessory")),sid+" missing pirate accessory")
        if sid in rs:
            r=rs[sid];need(r["prompt"]==s["canonical_prompt"],sid+" canonical prompt mismatch")
            need(r["parent_scene"]==p,sid+" parent mismatch")
            need(r["model_id"]==cfg["images"]["model_id"],sid+" season model mismatch")
            need(r["resolution"].lower()==cfg["images"]["model_params"]["resolution"].lower(),sid+" resolution mismatch")
            need(r["aspect_ratio"]=="16:9",sid+" aspect mismatch")
            need(s["historical_scope"] in r["prompt"],sid+" missing time/place")
            if not p:
                rr=r["reference_roles"]
                need(len(rr)==1 and rr[0]["role"]=="season_style_only",sid+" wrong anchor reference roles")
                if rr:need(rr[0].get("sha256")==digest(ROOT/"channel/assets/style_key.png"),sid+" style reference changed")
        seen.add(sid)
    for c in claims:
        need(c.get("type") in {"E", "F", "I"}, c["id"]+" invalid category; E=evidence, F=fictional framing, I=inference")
        need((c["id"] == "C0") == (c.get("type") == "F"), c["id"]+" category drift: only C0 is the shared fictional-framing row")
        need(bool(c.get("locator")),c["id"]+" missing passage locator")
        need(c["type"]=="F" or bool(c["sources"]),c["id"]+" factual claim lacks source")
        for x in c["sources"]:need(x in src,c["id"]+" unknown source "+x)
        need(set(c["scene_ids"])=={s["scene_id"] for s in scenes if c["id"] in s["claim_ids"]},c["id"]+" inconsistent scene mapping")
        if not draft:need(c["status"].startswith("checked") and c.get("checked_date"),c["id"]+" not checked")
    # Native parser is only invoked after proving every scene already has a unique ID.
    raw=(folder/"script.txt").read_text(encoding="utf-8-sig")
    headers=[line for line in raw.splitlines() if line.startswith(":::")]
    if all(re.match(r"^::: S\d{3,4} \| ",line) for line in headers) and len(headers)==len(scenes) and len(ss)==len(scenes):
        before=digest(folder/"script.txt")
        spec=importlib.util.spec_from_file_location("lp_package_validation",ROOT/"pipeline/lp.py")
        lp=importlib.util.module_from_spec(spec);spec.loader.exec_module(lp)
        title,native=lp.load_script(folder);nc=lp.load_claims(folder)
        need(before==digest(folder/"script.txt"),"Native parser changed script unexpectedly")
        need(title==d["title"],"Native title mismatch")
        need([x["id"] for x in native]==list(ss),"Native scene order differs")
        for a,b in zip(native,scenes):
            need(a["text"]==b["narration"],a["id"]+" native narration differs")
            need(a["same_as"]==b["parent_scene"],a["id"]+" native same-as differs")
        need({x["id"] for x in nc}==set(cs),"Native claim parser lost rows")
        if not draft:need(all(x["status"].startswith("checked") for x in nc),"Native claims remain unchecked")
    else: errors.append("Native script IDs/count invalid; skipped potentially mutating parser")
    thumbs=read(folder/"image_prompts.json")["thumbnail_requests"]
    need(len(thumbs)==3,"Need3 finished thumbnail specifications")
    for t in thumbs:
        need(bool(t["prompt"]) and bool(t["rationale"]),"Thumbnail missing concrete direction")
        need(len(t["composite"]["headline"].split())<=4,t["id"]+" headline over4 words")
        need(t["composite"]["visitor_pose"] in pose_map,t["id"]+" unknown thumbnail pose")
        need(all(x in ss for x in t["payoff_scene_ids"]),t["id"]+" payoff scene unknown")
        if d.get("pirate_hat"):need(t["composite"]["hat"],t["id"]+" hat missing")
    shorts=read(folder/"shorts_plan.json")["shorts"];need(len(shorts)==3,"Need3 Shorts")
    for x in shorts:
        need(x["from_scene"] in ss and x["to_scene"] in ss,x["id"]+" invalid boundaries")
        if x["from_scene"] in ss and x["to_scene"] in ss:
            order=list(ss);a=order.index(x["from_scene"]);b=order.index(x["to_scene"]);need(a<=b,x["id"]+" reversed cut")
            count=sum(len(scenes[i]["narration"].split()) for i in range(a,b+1))
            if not 90<=count<=175:warnings.append(x["id"]+f" needs duration/pacing review ({count} words)")
    snd=read(folder/"sound_plan.json");need(snd.get("status")!="director_specification_pending","Sound direction missing")
    for x in snd.get("cues",[]):need(x["scene_id"] in ss,"Sound cue scene missing")
    need(read(folder/"pronunciations.json").get("status")!="director_specification_pending","Pronunciation direction missing")
    for p in d["pilot"]:need(p in ss or p in {t["id"] for t in thumbs},"Pilot item unknown "+p)
    wardrobe=read(folder/"wardrobe_spec.json")
    need(bool(wardrobe.get("mode")),"Visitor wardrobe decision missing")
    if d.get("pirate_hat"):need((folder/"pirate_hat_spec.json").exists(),"Pirate hat implementation missing")
    if not draft:
        need(wardrobe.get("status")!="director_selection_pending","Wardrobe decision unresolved")
        review=read(folder/"review.json")
        for k in ["exact_script_critical_review","additional_slate_review_1","additional_slate_review_2"]:
            need(review.get(k)=="passed",k+" incomplete")
        need(read(folder/"director_to_claude.json")["status"]=="director_package_ready","Handoff not released")
        manifest=folder/"package_manifest.json";need(manifest.exists(),"Package manifest missing")
        if manifest.exists():
            for name,sha in read(manifest)["files"].items():
                need((folder/name).is_file() and digest(folder/name)==sha,"Manifest mismatch "+name)
    return {"folder":folder.name,"words":words,"shots":len(scenes),"illustrations":len(rs),"graphics":len(graphic_ids),"visitors":sum(bool(s["visitor"]) for s in scenes),"errors":errors,"warnings":warnings,"historical_and_media_review":"Not certified by this structural check"}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--folder");ap.add_argument("--draft",action="store_true");a=ap.parse_args()
    folders=[HERE/a.folder] if a.folder else [p for p in HERE.iterdir() if p.is_dir() and re.match(r"\d{2} - ",p.name)]
    result=[validate(p,a.draft) for p in sorted(folders)]
    print(json.dumps({"mode":"draft" if a.draft else "release","packages":result},ensure_ascii=False,indent=2))
    return 1 if any(x["errors"] for x in result) else 0
if __name__=="__main__":sys.exit(main())
