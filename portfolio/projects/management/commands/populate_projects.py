import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from projects.models import Project


class Command(BaseCommand):
    help = "Populates the database with 5 dummy projects with images"

    def handle(self, *args, **kwargs):
        self.stdout.write("🗑️  Cleaning old projects...")
        Project.objects.all().delete()

        projects_data = [
            # 1. SaaS / Web App
            {
                "slug": "saas-crm-platform",
                "category": "web",
                "is_featured": True,
                "image_url": "https://placehold.co/800x600/2563eb/ffffff/png?text=SaaS+CRM",
                "tools": "Django, HTMX, Tailwind, PostgreSQL",
                "github_url": "https://github.com/yourusername/crm",
                "live_url": "https://example.com",
                "title_en": "SaaS CRM Dashboard",
                "description_en": "A B2B CRM tool with real-time analytics, subscription management, and email automation.",
                "body_en": "Built a scalable multi-tenant architecture using Django Schema. Integrated Stripe for recurring payments and Celery for background email processing.",
                "title_fa": "داشبورد مدیریت مشتریان (CRM)",
                "description_fa": "ابزار CRM سازمانی با تحلیل‌های در لحظه، مدیریت اشتراک‌ها و اتوماسیون ایمیل.",
                "body_fa": "معماری چند مستاجری (Multi-tenant) با استفاده از اسکیماهای پستگرس. یکپارچه‌سازی با استرایپ برای پرداخت‌های دوره‌ای و سلری برای پردازش ایمیل‌ها.",
            },
            # 2. Fintech / API
            {
                "slug": "fintech-api-gateway",
                "category": "api",
                "is_featured": True,
                "image_url": "https://placehold.co/800x600/0f172a/ffffff/png?text=Secure+API",
                "tools": "DRF, Docker, Redis, JWT",
                "github_url": "https://github.com/yourusername/api",
                "live_url": None,
                "title_en": "Secure Banking Gateway",
                "description_en": "High-performance REST API handling 10k+ transactions/sec with bank-grade security.",
                "body_en": "Designed using Django Rest Framework with strict JWT throttling. Implemented Redis caching strategies to reduce database load by 40%.",
                "title_fa": "درگاه امن بانکی",
                "description_fa": "رست API با کارایی بالا که بیش از ۱۰ هزار تراکنش در ثانیه را با امنیت بانکی مدیریت می‌کند.",
                "body_fa": "طراحی شده با DRF و محدودیت‌های سخت‌گیرانه JWT. پیاده‌سازی استراتژی‌های کش Redis که بار دیتابیس را تا ۴۰٪ کاهش داد.",
            },
            # 3. Automation / Bot
            {
                "slug": "crypto-trading-bot",
                "category": "bot",
                "is_featured": False,
                "image_url": "https://placehold.co/800x600/f59e0b/ffffff/png?text=Crypto+Bot",
                "tools": "Python, AsyncIO, Binance API",
                "github_url": "https://github.com/yourusername/bot",
                "live_url": "https://t.me/yourbot",
                "title_en": "Crypto Arbitrage Bot",
                "description_en": "An automated bot that detects price differences across exchanges and executes trades.",
                "body_en": "Uses Python's AsyncIO for non-blocking websocket connections to Binance and KuCoin. Deployed on AWS Lambda for 24/7 uptime.",
                "title_fa": "ربات آربیتراژ ارز دیجیتال",
                "description_fa": "ربات خودکار که اختلاف قیمت‌ها را در صرافی‌های مختلف شناسایی و معامله می‌کند.",
                "body_fa": "استفاده از AsyncIO برای اتصال وب‌سوکت بدون وقفه به بایننس و کوکوین. دیپلوی شده روی AWS Lambda برای فعالیت ۲۴ ساعته.",
            },
            # 4. Real Estate / GeoDjango
            {
                "slug": "real-estate-platform",
                "category": "web",
                "is_featured": True,
                "image_url": "https://placehold.co/800x600/10b981/ffffff/png?text=Geo+Map",
                "tools": "GeoDjango, Leaflet.js, PostGIS, AWS S3",
                "github_url": "https://github.com/yourusername/realestate",
                "live_url": "https://example.com/homes",
                "title_en": "Smart Real Estate Map",
                "description_en": "Interactive property finder using geospatial data to filter homes by radius and amenities.",
                "body_en": "Leveraged PostGIS for spatial queries (e.g., 'Find homes within 5km of a subway'). Frontend built with Leaflet.js and optimized vector tiles.",
                "title_fa": "سامانه هوشمند املاک",
                "description_fa": "جستجوگر تعاملی ملک با استفاده از داده‌های جغرافیایی برای فیلتر بر اساس شعاع و امکانات.",
                "body_fa": "استفاده از PostGIS برای کوئری‌های مکانی (مثلاً خانه‌های تا ۵ کیلومتری مترو). فرانت‌اند ساخته شده با Leaflet.js و تایل‌های برداری بهینه.",
            },
            # 5. Scraper / Automation
            {
                "slug": "ecommerce-price-tracker",
                "category": "bot",
                "is_featured": False,
                "image_url": "https://placehold.co/800x600/6366f1/ffffff/png?text=Scraper",
                "tools": "Selenium, Celery, BeautifulSoup",
                "github_url": "https://github.com/yourusername/scraper",
                "live_url": None,
                "title_en": "Competitor Price Tracker",
                "description_en": "Distributed scraping system monitoring 50k+ products daily for e-commerce insights.",
                "body_en": "Orchestrated a fleet of headless browsers using Selenium Grid and Celery. Includes a dashboard for visualizing price trends over time.",
                "title_fa": "ردیاب قیمت رقبا",
                "description_fa": "سیستم خزش توزیع‌شده برای رصد روزانه قیمت بیش از ۵۰ هزار محصول.",
                "body_fa": "مدیریت ناوگانی از مرورگرهای بدون سر (Headless) با استفاده از Selenium Grid و Celery. شامل داشبورد برای مشاهده روند قیمت‌ها در طول زمان.",
            },
        ]

        self.stdout.write("🚀 Adding new projects with images...")

        for data in projects_data:
            # Create the project instance first
            project = Project(
                slug=data["slug"],
                category=data["category"],
                is_featured=data["is_featured"],
                tools=data["tools"],
                github_url=data["github_url"],
                live_url=data["live_url"],
                title_en=data["title_en"],
                description_en=data["description_en"],
                body_en=data["body_en"],
                title_fa=data["title_fa"],
                description_fa=data["description_fa"],
                body_fa=data["body_fa"],
            )

            # Download and save the image
            try:
                self.stdout.write(f"   Downloading image for {data['title_en']}...")
                response = requests.get(data["image_url"])
                if response.status_code == 200:
                    file_name = f"{data['slug']}.png"
                    project.image.save(
                        file_name, ContentFile(response.content), save=False
                    )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"   Failed to download image: {e}"))

            project.save()
            self.stdout.write(self.style.SUCCESS(f"   Created: {data['title_en']}"))

        self.stdout.write(self.style.SUCCESS("✅ Done! 5 Projects Added with Images."))
