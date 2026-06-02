serpApiKey = "https://serpapi.com/search?engine=google_jobs"
params = {
        'q':'Junior Software Developer',
        'location':'Waterdown',
        'api_key':'4283f57cada3ed115775418dff33d2550933323a2809c4429f07eaa2a7fb2ec7'
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
"""