import yaml

SOURCE_FILE = "_data/sources.yaml"
OUTPUT_FILE = "publications.md"

def load_publications(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return [pub for pub in data if pub.get("type") == "paper"]

def save_publications_md(publications, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("# Publications\n\n")
        for pub in publications:
            title = pub.get("description", "No Title") 
            date = pub.get("date", "Unknown Date")
            doi = pub.get("id", "").replace("doi:", "https://doi.org/")

            file.write(f"- **[{title}]({doi})** ({date})\n")

if __name__ == "__main__":
    publications = load_publications(SOURCE_FILE)
    save_publications_md(publications, OUTPUT_FILE)
    print(f"Updated {len(publications)} publications.")
