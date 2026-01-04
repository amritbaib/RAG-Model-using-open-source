import os
import re
import wikipedia


def sanitize_filename(title: str) -> str:
   
    return re.sub(r'[\\/*?:"<>|]', "_", title).strip()


def generate_corpus(search_term="nutrition and fat loss", num_articles=100, output_dir="all_articles"):
    os.makedirs(output_dir, exist_ok=True)

    articles = []  
    search_results = wikipedia.search(search_term, results=num_articles)

    for i, title in enumerate(search_results, 1):
        try:
            page = wikipedia.page(title, auto_suggest=False)
            articles.append((title, page.content))  

            sanitized = sanitize_filename(title)  
            filename = f"{sanitized}.txt"         
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(page.content)

        except Exception as e:  
            print(f"error processing '{title}': {str(e)}")
            continue

    print(f"\nCompleted! Saved {len(articles)} articles!")


if __name__ == "__main__":  
    generate_corpus()       