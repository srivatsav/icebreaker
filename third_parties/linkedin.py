import requests


def scrape_profile(profile_url: str):
    api_endpoint = (
        "https://gist.githubusercontent.com/srivatsav/d2a90731c46f7ef93b8db20e08612e50/raw"
        "/5a488ad198dccbc1c00c4384151dec9141b1c732/sri.json"
    )
    response = requests.get(
        api_endpoint, verify="/Users/srivatsav.gorti/Downloads/certs.pem"
    )
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None) and k not in ["certifications", "people_also_viewed"]
    }
    if data.get("profile_pic_url"):
        data.pop("profile_pic_url")
    if data.get("background_cover_image_url"):
        data.pop("background_cover_image_url")

    if data.get("experiences"):
        for dict in data.get("experiences"):
            dict.pop("company_linkedin_profile_url")
            dict.pop("logo_url")

    if data.get("education"):
        for dict in data.get("education"):
            dict.pop("logo_url")

    if data.get("activities"):
        for dict in data.get("activities"):
            dict.pop("link")

    if data.get("similarly_named_profiles"):
        for dict in data.get("similarly_named_profiles"):
            dict.pop("link")

    if data.get("articles"):
        for dict in data.get("articles"):
            dict.pop("link")
            dict.pop("image_url")

    return data
