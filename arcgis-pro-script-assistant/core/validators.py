def detect_crs_warning(user_prompt):

    keywords = ["buffer", "distance", "meters", "kilometers"]

    for word in keywords:
        if word.lower() in user_prompt.lower():

            return (
                "⚠️ Warning: Make sure your layer uses a projected CRS "
                "before performing distance-based analysis."
            )

    return None