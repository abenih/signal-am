# Contributing

1. Lexicon and gazetteer edits are plain YAML pull requests — the highest-value contribution.
   Every term needs `lang`, `term`, `weight`, and a `source`; health terms also need a named validator before merge.
2. Code: run `pytest` before opening a PR. No new runtime dependency without discussion in an issue first.
3. Never add a data source that is not public. Never add personal data, credentials, or `.env` files.
