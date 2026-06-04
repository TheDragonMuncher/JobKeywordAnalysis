serpApiKey = "https://serpapi.com/search?engine=google_jobs"
params = {
        'q':'Junior Software Developer',
        'location':'Waterdown',
        'api_key':
    }
claudePrompt = """
You are a job market analyst. Extract structured data from job postings.
Return ONLY valid JSON with these fields:
{
  "keywords": ["list of important terms"],
  "required_skills": ["must-have skills"],
  "nice_to_have_skills": ["preferred but optional skills"],
  "seniority_level": "junior|mid|senior|lead",
  "years_experience": number or null
}
No explanation. No markdown. JSON only. 
"""
