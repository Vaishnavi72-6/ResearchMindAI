import re

def extract_metadata(text):

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    title = ""
    authors = ""
    abstract = ""

    # Find title
    for line in lines:

        lower = line.lower()

        if (
            len(line) > 50
            and "received" not in lower
            and "accepted" not in lower
            and "doi" not in lower
            and "digital object identifier" not in lower
            and "member" not in lower
            and "abstract" not in lower
            and "department" not in lower
            and "university" not in lower
        ):
            title = line
            break

    # Find authors (next meaningful line after title)
    if title:

        title_index = lines.index(title)

        for line in lines[title_index + 1:]:

            lower = line.lower()

            if (
                len(line) > 5
                and "department" not in lower
                and "university" not in lower
                and "abstract" not in lower
            ):
                authors = line
                break

    # Extract abstract
    abstract_match = re.search(
        r"ABSTRACT(.*?)(INTRODUCTION|Keywords|Index Terms)",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if abstract_match:
        abstract = abstract_match.group(1).strip()

    return {
        "title": title,
        "authors": authors,
        "abstract": abstract[:1500],
        "preview": text[:500]
    }