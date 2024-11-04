from src.generators.seo_generator import AdvancedSEOBlogGenerator
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    # RSS feed URL
    RSS_URL = "https://rss.app/feeds/DMu9390HsjBLIdBo.xml"
    
    try:
        # Initialize generator
        generator = AdvancedSEOBlogGenerator()
        
        # Process RSS feed
        generator.process_feed(RSS_URL)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()