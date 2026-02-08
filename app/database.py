def load_quotes():
    with open("data/quotes.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_quote(quote: str):
    with open("data/quotes.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{quote}")