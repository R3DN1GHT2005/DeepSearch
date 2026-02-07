# Google Advanced Search Tool

**Desktop application for building advanced Google search queries using Google operators.**

---

## 🔍 Search Operators

### Primary Keyword / Phrase
The main search term that forms the base of your query.

**Exact Match Checkbox:** Wraps the keyword in quotes to search for the exact phrase.
```
Input: machine learning
Without exact: machine learning
With exact: "machine learning"
```

---

### Exclude Words `(-)`
Removes pages containing specific terms from search results. Each excluded word gets a minus operator.

```
Input: free, trial, ads
Generated: -free -trial -ads
```

**Use case:** Remove unwanted commercial content, spam, or irrelevant results.

---

### OR Terms `(OR)`
Finds pages containing **at least one** of the specified terms. All terms are wrapped in parentheses.

```
Input: python, java, javascript
Generated: (python OR java OR javascript)
```

**Use case:** Search for synonyms or alternative technologies simultaneously.

---

### Target Domain `(site:)`
Restricts search results to a specific website or domain.

```
site:github.com          → Only GitHub
site:edu                 → Only educational institutions
site:wikipedia.org       → Only Wikipedia
```

**Use case:** Search within a trusted source or specific platform.

---

### File Extension `(filetype:)`
Finds downloadable files of specific formats.

```
filetype:pdf             → PDF documents
filetype:xlsx            → Excel spreadsheets
filetype:pptx            → PowerPoint presentations
filetype:docx            → Word documents
```

**Use case:** Find documentation, research papers, or data files.

---

### Text in Page Title `(intitle:)`
Searches for text specifically within the HTML `<title>` tag of webpages.

```
intitle:tutorial         → Pages with "tutorial" in title
intitle:"best practices" → Exact phrase in title
```

**Use case:** Find guides, tutorials, or specific types of content.

---

### Text in URL Path `(inurl:)`
Searches for text within the webpage's URL structure.

```
inurl:admin              → URLs containing "admin"
inurl:documentation      → URLs with "documentation" path
```

**Use case:** Find specific sections of websites or admin panels.

---

### Date Filters `(before: / after:)`
Filters results by Google's index date. Format: **YYYY-MM-DD**

```
after:2024-01-01         → Content indexed after Jan 1, 2024
before:2023-12-31        → Content indexed before Dec 31, 2023
```

**Use case:** Find recent information or historical content.

---

## 🛠️ Specialized Operators

### Define `(define:)`
Gets dictionary definitions and word usage.
```
define:algorithm         → Definition of "algorithm"
```

### Cache `(cache:)`
Views Google's cached (stored) version of a webpage.
```
cache:example.com        → Cached version of example.com
```

**Use case:** View a page that's down or has changed.

### Link `(link:)`
Finds pages that contain links to a specific URL.
```
link:wikipedia.org       → Pages linking to Wikipedia
```

---
