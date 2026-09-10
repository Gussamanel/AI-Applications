# AI Applications

A collection of six AI and machine-learning applications extracted from the accompanying coursework PDFs.

## Applications

| Directory | Application | Main techniques |
| --- | --- | --- |
| [geotiff-classifier](apps/geotiff-classifier) | GeoTIFF land-cover classification | PyTorch CNNs, spatial cross-validation |
| [dialog-system](apps/dialog-system) | Multi-domain conversational assistant | Keyword/entity extraction, pandas queries |
| [alphago-mcts](apps/alphago-mcts) | Generalized tic-tac-toe game player | Monte Carlo Tree Search, UCT |
| [tictactoe-mcts-random-forest](apps/tictactoe-mcts-random-forest) | Tic-tac-toe game-playing agent | MCTS, random forest board evaluation |
| [movie-recommender](apps/movie-recommender) | Content-based movie recommender | Genre profiles, cosine similarity |
| [air-quality-clustering](apps/air-quality-clustering) | Air-quality classification experiment | K-means, train/test evaluation |
| [reports](reports) | Original source documents | Six original PDF reports |

Each application directory contains `report-extracted.txt`, a searchable text extraction, and `source-listing.md`, a page-labelled extraction of the code-bearing sections. The PDFs in `reports/` are retained as the authoritative source.

## Important limitations

The reports reference local datasets and, in some cases, notebook state or saved model weights that were not included in the source folder. The extracted listings are therefore archival source material rather than guaranteed turnkey applications. Dataset paths and dependencies should be updated before running them.

## Source documents

The original PDFs are preserved verbatim in [reports](reports). The files were provided by the project author.