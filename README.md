# XML Attribute Extraction Challenge



## Overview

This script extracts all `<doc-number>` values from a given XML patent file, prioritizing:

1. Entries where `format="epo"`

2. Entries where `format="original"` (from `load-source="patent-office"`)



\## Assumptions

* All XML files are utf-8 encoded
* The XML may have missing tags or malformed attributes.
* We skip records missing `<doc-number>`.
* Only `<document-id>` nodes under `<application-reference>` are relevant.



\## Setup

Install dependencies and run using **uv**:

```uv sync```

Run this to extract the document numbers:

```uv run python extract\_doc\_numbers.py sample.xml```



