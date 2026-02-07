import urllib.parse
import re
from datetime import datetime

class QueryArchitect:
    def __init__(self):
        self.operator_map = {
            "site": "site:", "filetype": "filetype:", "intitle": "intitle:",
            "inurl": "inurl:", "intext": "intext:", "define": "define:",
            "related": "related:", "before": "before:", "after": "after:",
            "source": "source:", "weather": "weather:", "stocks": "stocks:",
            "cache": "cache:", "link": "link:"
        }

    def validate_date(self, date_str):
        """Validate date format YYYY-MM-DD"""
        if not date_str:
            return True
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def build_google_url(self, raw_data):
        query_parts = []
        
        if raw_data.get("before") and not self.validate_date(raw_data.get("before")):
            return "ERROR: Invalid 'before' date format. Use YYYY-MM-DD"
        if raw_data.get("after") and not self.validate_date(raw_data.get("after")):
            return "ERROR: Invalid 'after' date format. Use YYYY-MM-DD"
        
        base = raw_data.get("keyword", "").strip()

        if base:
            if raw_data.get("exact_match") is True:
                query_parts.append(f'"{base}"')
            else:
                query_parts.append(base)
        
        exclude = raw_data.get("exclude", "").strip()
        if exclude:
            exclude_terms = [f"-{term.strip()}" for term in exclude.split(",") if term.strip()]
            query_parts.extend(exclude_terms)
        
        or_terms = raw_data.get("or_terms", "").strip()
        if or_terms:
            or_words = [term.strip() for term in or_terms.split(",") if term.strip()]
            if or_words:
                query_parts.append("(" + " OR ".join(or_words) + ")")

        for key, prefix in self.operator_map.items():
            value = raw_data.get(key, "").strip()
            if value:
                query_parts.append(f"{prefix}{value}")

        if not query_parts:
            return ""

        final_query = " ".join(query_parts)
        return f"https://www.google.com/search?q={urllib.parse.quote(final_query)}"
    
    def build_preview_query(self, raw_data):
        """Build preview string without encoding"""
        query_parts = []
        
        base = raw_data.get("keyword", "").strip()
        if base:
            if raw_data.get("exact_match") is True:
                query_parts.append(f'"{base}"')
            else:
                query_parts.append(base)
        
        exclude = raw_data.get("exclude", "").strip()
        if exclude:
            exclude_terms = [f"-{term.strip()}" for term in exclude.split(",") if term.strip()]
            query_parts.extend(exclude_terms)
        
        or_terms = raw_data.get("or_terms", "").strip()
        if or_terms:
            or_words = [term.strip() for term in or_terms.split(",") if term.strip()]
            if or_words:
                query_parts.append("(" + " OR ".join(or_words) + ")")

        for key, prefix in self.operator_map.items():
            value = raw_data.get(key, "").strip()
            if value:
                query_parts.append(f"{prefix}{value}")

        return " ".join(query_parts) if query_parts else "(empty query)"