# YouTube SEO playbook

## AI disclosure decision, 9 October 2026
After discussing the current Studio question and the ambiguity in YouTube's Help examples, the owner explicitly chose **No for the current two episodes and six Shorts**. The basis is the actual questionnaire: stylised animation, no impersonation or altered real footage, and AI theme music used as background rather than as the video's main focus. The music remains AI-generated; never record or describe it as human-made. Omit optional AI/tool-production statements from public descriptions, channel copy and upload templates per the owner's 9 October request. Preserve source references and required credits, keep internal AI provenance accurate, and do not claim human-only or handmade production. Mandatory platform disclosure is assessed separately. The temporary switch to Yes is superseded for these eight uploads. For future videos, assess their actual visuals and audio against the current platform question; this is not blanket permission to select No for photorealistic scenes, impersonation, altered footage or music-focused videos. Record ambiguities and verify the saved choice. See `handoff/ai_disclosure_decision_2026-10-09.json`.

Researched 2026-10-07 (YouTube Help: how search works, tags, description tips, hashtags, spam policy; Creator Liaison / Todd Beaupre Q&A). Applied first to episode 001.

## What actually matters, in order
1. Title: the field YouTube weighs most. A real question people type, 40-65 characters, with the place/era phrase in it. Never a keyword tail.
2. Thumbnail + watch time: search ranks relevance, engagement (watch time for that search) and quality/trust. Metadata only gets the video into the race.
3. Description opening (first 2 sentences, about 150 characters show in search): name the main phrases naturally once, e.g. 'daily life in medieval <place>', 'the Middle Ages'. Unique per video, under 5,000 bytes, no < or >.
4. Chapters with descriptive labels (they can show as key moments in Google): first at 0:00, each at least 10 seconds.
5. Captions (upload our own .srt), playlist with a descriptive name and description, the visible sources list and fact-check line (trust signal).
6. Hashtags: exactly 3 at the end of the description, specific to the topic (#medievallondon over #london). Never in the title.
7. Tags: minimal weight (YouTube's words). Use them for real searched phrases the video answers and common misspellings ('mediaeval', 'midieval'). 500-character limit: commas count and every tag with a space costs 2 extra. Studio's counter is final.

## Method per episode
- Pull YouTube autocomplete for 20-30 seeds (place, era, 'life in medieval', 'what did medieval people', 'a day in', the episode's strongest topics). No script is kept: query YouTube's autocomplete in the browser or with a short throwaway script, and save the results as the episode's `build/seo/autocomplete.json` (episode 002's shows the shape). Use only phrases the video truly answers.
- Drop tags whose autocomplete shows another intent (episode 001: '1390' = motorbikes and CPUs; 'medieval times' = a US dinner theatre) and names the narration never says.
- Don't target phrases that would mislead (e.g. 'medieval peasant' for a townspeople episode; 'worst medieval jobs' list searches). YouTube's spam policy bans misleading metadata and keyword stuffing; never paste tag lists into the description.
- Clone check on the final title (exact phrase and formula, sorted by upload date) at packaging and again on upload day; never reuse a title another channel published in the last 60 days, and prefer a title built on the episode's own angle over the trending formula.
- 7-14 days after release: Analytics > Reach > Traffic source: YouTube search. Add only true terms; consider a title test after 2-3 weeks if search impressions stay low.

## Other reach levers (ranked)
- 1. (Done for episode 001 before launch; kept as a record.) Before 10 Oct 19:00 (Sofia): in Studio > Content > this video > Details, paste description_full and replace the 25 tags with the 22 above. They come to 497/500 under the strict count (commas included, +2 for each tag containing a space) and 453 with commas only. Studio's own counter is final: if it shows more than 500, drop 'medieval history' first. Leave the title and thumbnail as they are. Then bring episodes/001-medieval-london-day/youtube_setup.md in line with Studio: line 18 (it still lists the old 18 tags, 326 characters), line 22 (the playlist is 'Medieval Life: How People Actually Lived', not 'Medieval Life (new)'), the description block in lines 24-64, and the hashtags on line 64. No project files were edited in this review.
- 2. Shorts cut from the finished render. This is the biggest reach lever for a zero-subscriber channel: Shorts reach people who don't subscribe, and each can link to the full video. Set each Short's related video to episode 001. Topics, all true to the video: (a) 'Did Medieval People Really Drink Beer Instead of Water?' (the autocomplete 'what did medieval people drink'; the video's answer is that it's half true, because the Great Conduit piped in spring water). (b) Gong farmers and Richard the Raker, 1326 ('one of the worst jobs in the city, but it pays well'). (c) '7 years, no wife': the apprenticeship terms, which match the thumbnail. If reframing to 9:16 needs any new images, state the count and cost first (AGENTS.md hard rule 5).
- 3. Check search terms 7-14 days after release: Analytics > Reach > Traffic source: YouTube search, plus the Research tab. Add to the description or tags only terms the video really covers. If search impressions stay low after 2-3 weeks, test title alternative 1 or 2. Use Test & Compare if the channel has title testing; otherwise make one manual swap and compare a week before with a week after.
- 4. Pinned comment at publish: one question that invites replies, e.g. 'London, 1390: would you rather sign on as an apprentice for seven years with no marrying, or be a well-paid gong farmer?' Reply to early comments. In suggested and browse, how viewers respond counts for much more than keywords.
- 5. Playlist: once the video is public, add a line under CHAPTERS reading 'Playlist: Medieval Life: How People Actually Lived', followed by its link. Give the playlist a short, true description that carries the main phrases, e.g. 'Daily life in the Middle Ages, one real place and year per episode. Every claim sourced.' Playlists can show up in search on their own.
- 6. Optional: more descriptive chapter labels, with exactly the same timestamps, which can show as key moments in Google search: 0:00 Cold open / 1:00 Woken by bells / 2:20 Breakfast and the beer-or-water myth / 3:25 Work: apprentices, sunrise to sunset / 4:58 Dinner: takeaway pies from a cookshop / 5:56 The streets: toilets, cesspits and gong farmers / 7:06 Free time: football, archery and the alehouse / 8:12 The last bell: curfew and the Tun. The render has no on-screen chapter cards, so nothing would clash. The package above keeps the current labels exactly; this swap is the owner's call.
- 7. Hashtags are already in description_full: #medievallondon #medievalhistory #middleages replace #history #medievalhistory #london. The reasoning: #history and #london are very broad tags where a new video gets buried, and narrower topic tags give it a better chance with viewers who want this subject. Keep exactly three, at the end, none in the title.
- 8. Community post on launch day, if Posts are available on the channel: the thumbnail plus a two-option poll (apprentice vs gong farmer). Low impact at zero subscribers, but it costs nothing.
- 9. End screen (subscribe plus next episode) once episode 2 exists, as already planned.
- 10. Guardrail: never paste a list of tags or repeated keyword lines into the description. Don't add 'medieval peasant', castle or knight tags, which describe a different subject, and don't add 'worst medieval jobs' list-style tags. Gong farming is called one of the worst jobs in the city, but people searching that phrase expect a ranked list, which this video isn't. Both kinds fall under YouTube's policy on misleading metadata.

## Sources
Add tags to your YouTube videos - YouTube Help: https://support.google.com/youtube/answer/146402
Find playlists & videos using hashtags - YouTube Help: https://support.google.com/youtube/answer/6390658
How YouTube search works - YouTube Help: https://support.google.com/youtube/answer/16090438
On YouTube's Recommendation System (Cristos Goodrow, VP Engineering, Sept 2021): https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/
Social Media Today / Todd Beaupré Q&A (category is a minor factor): https://www.socialmediatoday.com/news/youtube-launches-new-q-and-a-shorts-series-for-creator-questions/725188/
Social Media Today / Todd Beaupré Q&A (misspellings in tags): https://www.socialmediatoday.com/news/youtube-launches-new-q-and-a-shorts-series-for-creator-questions/725188/
Social Media Today, 'YouTube Launches Q&A Shorts Series for Creator Questions' (Aug 2024, answers by Todd Beaupré, posted by Creator Liaison Rene Ritchie): https://www.socialmediatoday.com/news/youtube-launches-new-q-and-a-shorts-series-for-creator-questions/725188/
Spam Policy - YouTube Help: https://support.google.com/youtube/answer/2801973
Tips for video descriptions - YouTube Help: https://support.google.com/youtube/answer/12948449
Video Chapters - YouTube Help: https://support.google.com/youtube/answer/9884579
Video SEO Best Practices | Google Search Central: https://developers.google.com/search/docs/appearance/video
Videos | YouTube Data API (description max 5000 bytes): https://developers.google.com/youtube/v3/docs/videos
Videos | YouTube Data API (snippet.tags[] counting rules): https://developers.google.com/youtube/v3/docs/videos
Videos | YouTube Data API (title max 100 characters): https://developers.google.com/youtube/v3/docs/videos
YouTube recommendations - How YouTube Works: https://www.youtube.com/howyoutubeworks/product-features/recommendations/
