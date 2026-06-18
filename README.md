# Dataset Tools

Dataset preprocessing, cleaning, and quality validation toolkit.

## Features
- Automated data profiling (types, distributions, missing values)
- Deduplication with locality-sensitive hashing
- Train/val/test split with stratification
- Data versioning with DVC integration

## CLI
```bash
dataset profile --input data.csv --output report.html
dataset clean --input raw.csv --output clean.csv --dedup --impute
dataset split --input clean.csv --ratios 0.8,0.1,0.1
```

## License
MIT
