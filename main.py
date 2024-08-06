import tldextract
import Levenshtein as lv

legitimate_domains = ['example.com', 'google.com', 'facebook.com']

test_urls = [
    'http://example.co',
    'http://examp1e.com',
    'https://www.google.security-update.com',
    'https://faceb00k.com/login',
    'https://google.com'
]


def extract_domain_parts(url):
    extracted = tldextract.extract(url)
    return extracted.subdomain, extracted.domain, extracted.suffix


def is_misspelled_domain(domain, legitimate_domains, threshold=0.9):
    for legitimate_domain in legitimate_domains:
        similarity = lv.ratio(domain, legitimate_domain)
        if similarity >= threshold:
            return False
    return True


def is_phishing_url(url, legitimate_domains):
    subdomain, domain, suffix = extract_domain_parts(url)

    # Check if it is a known legitimate domain
    if f"{domain}.{suffix}" in legitimate_domains:
        return False

    # Check for misspelled
    if is_misspelled_domain(domain, legitimate_domains):
        print(f"Potential phishing detected: {url}")
        return True

    return False


if __name__ == "__main__":
    for url in test_urls:
        is_phishing_url(url, legitimate_domains)