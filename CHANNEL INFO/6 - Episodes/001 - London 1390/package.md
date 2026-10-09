# Package: What Did People in Medieval London Actually Do All Day?

## Titles
1. What Did People in Medieval London Actually Do All Day? (main; proven question type)
2. You Wake Up in London, 1390. Here's Your Day.
3. Medieval London Ran on Bells. Could You Last a Day?

## Thumbnails (made with Higgsfield's thumbnail-generation guide)
Each background is a 4K Nano Banana Pro render made for the thumbnail (one focal point, high contrast, empty space for the Visitor and the headline, no text in the image). The Visitor is composited from the pose library, large and chest-up, and the headline is overlaid in the "Beast" style (heavy condensed caps, thick stroke, hard shadow). Sources are in `thumbs/`.

| File | Framework | Pose | Headline | Chip |
|---|---|---|---|---|
| `thumbnail_D.jpg` (NEW LEAD, = `thumbnail.jpg`) | Posed portrait + story object, from the thumbnail playbook (channel/thumbnails.md): the Visitor horrified by his apprenticeship contract while the master glares | closeup-horrified-contract | 7 YEARS. NO WIFE. | LONDON 1390 |
| `thumbnail_A.jpg` (A/B test option) | Posed portrait + landscape: one lantern in a dark lane | closeup-terrified | AFTER DARK? | LONDON 1390 |
| `thumbnail_B.jpg` | Repetition + posed portrait: three sleeping strangers | closeup-worried | YOUR BEDMATES | LONDON 1390 |
| `thumbnail_C.jpg` | Size difference: a giant bell | sit-cover-ears (cropped) | 100 ALARMS | LONDON 1390 |

Upload D as the lead. In A/B testing add A (AFTER DARK?) as the structurally different second option; YouTube picks by watch-time share. Truth check: C15 (at least seven years) and C16 (indentures banned marriage).

Command (D): `python pipeline/lp.py thumb 001-medieval-london-day episodes/001-medieval-london-day/thumbs/bg_contract.png "7 YEARS.|NO WIFE." "LONDON 1390" --side left --text-pos bottom --accent --pose closeup-horrified-contract --pose-x 0.76 --pose-size 0.92 --bg-dim 0.75` (measured: Visitor face 0.81 vs brightest background 0.58; hoodie 0.51 vs background median 0.36).

Command (lead): `python pipeline/lp.py thumb 001-medieval-london-day episodes/001-medieval-london-day/thumbs/bg_after_dark.png "AFTER|DARK?" "LONDON 1390" --side left --text-pos top --accent --pose closeup-terrified --pose-x 0.74 --pose-size 0.88 --flip false`

## Description
```
What would a normal day in medieval London actually be like for you?

You wake up in London in 1390, beside three strangers, with no clock and a church bell ringing. From breakfast that isn't a meal, to takeaway pies, gong farmers and a city curfew, this is how an ordinary Londoner's day ran: on bells, daylight and a lot of rules.

CHAPTERS
0:00 Cold open
1:00 Woken by bells
2:20 Breakfast and water
3:25 Work: sunrise to sunset
4:58 Dinner from a cookshop
5:56 The streets
7:06 Free time
8:12 The last bell

SOURCES
Caroline M. Barron, London in the Later Middle Ages (2004)
Barbara A. Hanawalt, Growing Up in Medieval London (1993)
H. T. Riley (ed.), Memorials of London and London Life (1868)
Martha Carlin, "Fast Food and Urban Living Standards in Medieval England" (1998)
C. M. Woolgar, The Culture of Food in England, 1200-1500 (2016)
Judith M. Bennett, Ale, Beer, and Brewsters in England (1996)
Ernest L. Sabine, "Latrines and Cesspools of Mediaeval London" (1934) and "City Cleaning in Mediaeval London" (1937)
R. R. Sharpe (ed.), Calendar of Coroners Rolls of the City of London, 1300-1378 (1913)
John Stow, A Survey of London (1598)
Ian Mortimer, The Time Traveller's Guide to Medieval England (2008)
Liber Albus: The White Book of the City of London (1419), trans. H. T. Riley (1861)
R. R. Sharpe (ed.), Calendar of Letter-Books of the City of London (1899-1912)
H. M. Chew and W. Kellaway (eds), London Assize of Nuisance 1301-1431 (1973)
Dolly Jørgensen, "Modernity and Medieval Muck", Nature and Culture 9.3 (2014)
Ruth Mazo Karras, Common Women: Prostitution and Sexuality in Medieval England (1996)
John Schofield, Medieval London Houses (1994)

On-screen documents: Great Conduit (begun 1245); Articles of the Spurriers (1345); Statute of Labourers (1351); London cooks' price list (1378); city street-cleaning order (1357); coroner's roll (1326); mayor's proclamation against football (1314, Liber Memorandorum fol. 66); order of Edward III (1363); Statutes of the City of London (1285); the Tun on Cornhill (built 1282, per Stow).
Every claim in this video was checked against its source; the full claim sheet with page references is available on request.

Music: "Life, Previously" theme, made for this channel.
```

## Upload settings
- Tags: medieval london, medieval life, middle ages, daily life in history, history explained, medieval england
- Playlist: Medieval Life
- End screen: episode 2 plus subscribe
- Captions: captions.srt
- Altered or synthetic content: No (clearly animated)
