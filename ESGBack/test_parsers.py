import sys
import os

# Add ESGBack directory to python path
sys.path.append(r"c:\Users\Admin\Desktop\практика проект\ESGBack")

# Mock Django setup to avoid import errors if any are triggered
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ESGBack.settings')
django.setup()

from v1.parsers.NewsParsers.EsgnewscomParser import Parse_EsgnewscomRuNews, Parse_EsgnewscomEnNews

from v1.parsers.NewsParsers.InformkzParser import Parse_informkzRuNews
from v1.parsers.NewsParsers.GovkznewsParser import Parse_GovkznewsRu
from v1.parsers.CourseParsers.CsdCenterKzCourseParser import Parse_CsdCenterKzRuCourses

print("Testing Parse_EsgnewscomRuNews...")
try:
    articles_ru = Parse_EsgnewscomRuNews()
    print(f"Success! Found {len(articles_ru)} Russian ESG News articles.")
    if articles_ru:
        print(f"Sample article: {articles_ru[0].title} | Link: {articles_ru[0].url}")
except Exception as e:
    print(f"Error in EsgnewscomRuNews: {e}")

print("\nTesting Parse_informkzRuNews...")
try:
    articles_informkz = Parse_informkzRuNews(max_pages=2)
    print(f"Success! Found {len(articles_informkz)} Inform.kz articles.")
    if articles_informkz:
        print(f"Sample article: {articles_informkz[0].title} | Link: {articles_informkz[0].url}")
except Exception as e:
    print(f"Error in InformkzRuNews: {e}")

print("\nTesting Parse_GovkznewsRu...")
try:
    articles_gov = Parse_GovkznewsRu()
    print(f"Success! Found {len(articles_gov)} Gov.kz articles.")
    if articles_gov:
        print(f"Sample article: {articles_gov[0].title} | Link: {articles_gov[0].url}")
except Exception as e:
    print(f"Error in GovkznewsRu: {e}")

print("\nTesting Parse_CsdCenterKzRuCourses...")
try:
    courses = Parse_CsdCenterKzRuCourses()
    print(f"Success! Found {len(courses)} CSD Center courses.")
    if courses:
        print(f"Sample course: {courses[0].title} | Link: {courses[0].url}")
except Exception as e:
    print(f"Error in CsdCenterKzRuCourses: {e}")

print("\nTesting Parse_EsgnewscomEnNews...")
try:
    articles_en = Parse_EsgnewscomEnNews()
    print(f"Success! Found {len(articles_en)} English articles.")
    if articles_en:
        print(f"Sample article: {articles_en[0].title} | Link: {articles_en[0].url}")
except Exception as e:
    print(f"Error in EsgnewscomEnNews: {e}")
