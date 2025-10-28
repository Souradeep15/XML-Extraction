from lxml import etree
import sys

def load_xml(file_path):
    try:
        parser = etree.XMLParser(recover=True)  # allows broken XML
        with open(file_path, "r", encoding="utf-8") as f:
            return etree.parse(f, parser) #parse xml
    except Exception as e:
        print(f"Error loading XML: {e}")
        sys.exit(1)

def extract_doc_numbers(tree):
    doc_numbers = {"epo": [], "original": []} #initialte arrays to maintain order

    for doc_id in tree.xpath("//document-id"):
        format_type = doc_id.get("format", "").lower() #get the format
        load_source = doc_id.get("load-source", "").lower() #get the load source
        doc_number = doc_id.findtext("doc-number") #got the doc number

        if not doc_number:
            continue  # skip incomplete records

        if format_type == "epo":
            doc_numbers["epo"].append(doc_number) #append all epo doc numbers
        elif load_source == "patent-office":
            doc_numbers["original"].append(doc_number) #append all the patent-office numbers

    return doc_numbers["epo"] + doc_numbers["original"] #maintains order

if __name__ == "__main__":
    xml_file = sys.argv[1]
    tree = load_xml(xml_file) #returns the formatted tree
    ordered_doc_numbers = extract_doc_numbers(tree) #extracts doc numbers
    print(ordered_doc_numbers)
