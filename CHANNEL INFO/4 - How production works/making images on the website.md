# Making the images yourself on higgsfield.ai

Each stage has a helper page in this folder: open it in Chrome (double-click the `.html` file). It shows the exact settings, a **Copy prompt** button for every image, what to check before you download, and a **Done** tick that remembers your progress.

## One-time Chrome setting (before stage 3)
Chrome Settings > Downloads > Location > Change, and choose the project's `inbox` folder (its path is on the stage 3 and 4 pages, with a Copy button). Imports then only ever see Higgsfield downloads. Switch it back when you finish a session if you like.

## The stages
| Stage | Page | You make | Then |
|---|---|---|---|
| 1 | `1-style-key.html` | One test scene on 4 models, 4 images each. Download only your favourite. | `python pipeline/lp.py pick style-key "<file>" --model "<model name>"`, or tell Claude which model and where the file is. |
| 2 | `2-visitor-sheet.html` (made by `python pipeline/lp.py brief --visitor-sheet`) | The Visitor model sheet. Regenerate until you love one, then download it. | `python pipeline/lp.py pick visitor-sheet "<file>"` |
| 3 | `3-backgrounds-<episode>.html` (made by `python pipeline/lp.py brief <episode>`) | Every background, in order, one download per card | `python pipeline/lp.py import <episode> inbox`, then `python pipeline/lp.py sheet <episode>` |
| 4 | `4-poses.html` (made by `python pipeline/lp.py brief --poses`) | Every Visitor pose on green, in order, one download per card | `python pipeline/lp.py import --poses inbox`, then `python pipeline/lp.py sheet --poses` |

## How one image goes (stages 3 and 4)
1. Attach the reference image once with **+** (paste its path from the page into the file dialog). It stays attached.
2. On the page, click **Copy prompt** on the highlighted card.
3. In Higgsfield, click the prompt box, press **Ctrl+A**, then **Ctrl+V**, and generate (2 images).
4. Check the image against the page's list. Download the better one (or generate again if neither passes).
5. Tick **Done**. The next card lights up.

**The one rule that matters:** download exactly one image per card, in the page's order. The import matches downloads to cards by the order they were downloaded. You can stop any time: import at the end of each session, and next time carry on from the highlighted card. Imported files move to `inbox/imported/`, so they're never used twice.

**To redo an image later:** delete it from the episode's `images/` folder, run `python pipeline/lp.py brief <episode>` again (the new page lists only the missing ones), generate it, and import.
