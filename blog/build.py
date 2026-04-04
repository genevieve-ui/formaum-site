#!/usr/bin/env python3
"""
Blog post generator for formaum.com
Reads a JSON config and generates a full HTML blog post using the approved template.

Usage: python3 build.py config.json
"""

import json
import sys
import os
from datetime import date

def build_faq_schema(faqs):
    if not faqs:
        return ""
    entities = []
    for f in faqs:
        entities.append(f'{{"@type":"Question","name":"{f["q"]}","acceptedAnswer":{{"@type":"Answer","text":"{f["a"]}"}}}}')
    return f'''
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{",".join(entities)}]
    }}
    </script>'''

def build_faq_html(faqs):
    if not faqs:
        return ""
    items = []
    for i, f in enumerate(faqs):
        open_class = ' open' if i == 0 else ''
        items.append(f'''
            <div class="faq-item{open_class}">
                <div class="faq-q">{f["q"]}</div>
                <div class="faq-a">{f["a"]}</div>
            </div>''')
    return f'''
        <hr class="divider">
        <div class="faq-section">
            <h2>Frequently Asked Questions</h2>
            {"".join(items)}
        </div>'''

def build(config):
    c = config
    slug = c["slug"]
    title = c["title"]
    subtitle = c["subtitle"]
    meta_desc = c["meta_description"]
    keywords_meta = ", ".join(c["keywords"])
    keywords_json = json.dumps(c["keywords"])
    blog_label = c.get("blog_label", "GHL Migration")
    reading_time = c.get("reading_time", "7 min read")
    content_html = c["content_html"]
    faqs = c.get("faq", [])
    today = c.get("date", date.today().isoformat())
    breadcrumb_label = c.get("breadcrumb_label", title[:40])

    faq_schema = build_faq_schema(faqs)
    faq_html = build_faq_html(faqs)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Formaum</title>
    <meta name="description" content="{meta_desc}">
    <meta name="keywords" content="{keywords_meta}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{subtitle}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://formaum.com/blog/{slug}.html">
    <meta property="article:author" content="Genevieve Claire">
    <meta property="article:published_time" content="{today}">
    <link rel="canonical" href="https://formaum.com/blog/{slug}.html">

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title}",
        "author": {{
            "@type": "Person",
            "name": "Genevieve Claire",
            "jobTitle": "Operations Strategist",
            "url": "https://formaum.com",
            "sameAs": ["https://linkedin.com/in/genevieveclaire"]
        }},
        "publisher": {{ "@type": "Organization", "name": "Formaum", "url": "https://formaum.com" }},
        "datePublished": "{today}",
        "dateModified": "{today}",
        "description": "{meta_desc}",
        "mainEntityOfPage": "https://formaum.com/blog/{slug}.html",
        "keywords": {keywords_json},
        "articleSection": "{blog_label}"
    }}
    </script>

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://formaum.com" }},
            {{ "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://formaum.com/blog/" }},
            {{ "@type": "ListItem", "position": 3, "name": "{breadcrumb_label}" }}
        ]
    }}
    </script>
    {faq_schema}

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --navy-deep: #0D1B2A; --navy: #1B2D45; --navy-mid: #243B55; --slate: #34506B;
            --blue-accent: #4A8FD4; --blue-light: #6AADDD;
            --warm-white: #FAF9F6; --cream: #F3F1EC; --ice: #EDF2F8; --ice-blue: #E4EBF5;
            --text-dark: #0D1B2A; --text-body: #2A3E55; --text-muted: #6B819A;
            --text-light: #F0EDE8; --text-light-muted: rgba(240, 237, 232, 0.6);
            --red-soft: #E74C3C; --green-soft: #2ECC71;
        }}
        html {{ scroll-behavior: smooth; }}
        body {{ font-family: 'Montserrat', sans-serif; font-weight: 400; color: var(--text-dark); line-height: 1.6; background: var(--warm-white); -webkit-font-smoothing: antialiased; }}
        h1, h2, h3 {{ font-family: 'Montserrat', sans-serif; font-weight: 400; letter-spacing: -0.5px; line-height: 1.15; }}
        nav {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; padding: 20px 48px; display: flex; justify-content: space-between; align-items: center; background: rgba(13, 27, 42, 0.92); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-bottom: 1px solid rgba(255,255,255,0.06); }}
        .logo {{ font-size: 18px; font-weight: 500; color: var(--text-light); text-decoration: none; letter-spacing: -0.5px; }}
        .nav-right {{ display: flex; align-items: center; gap: 28px; }}
        .nav-link {{ font-size: 13px; color: var(--text-light-muted); text-decoration: none; transition: color 0.3s; }}
        .nav-link:hover {{ color: var(--text-light); }}
        .nav-cta {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 1.5px; color: var(--navy-deep); background: var(--blue-accent); padding: 10px 22px; border-radius: 4px; text-decoration: none; transition: all 0.3s; }}
        .nav-cta:hover {{ background: var(--blue-light); }}
        .breadcrumb {{ max-width: 720px; margin: 0 auto; padding: 100px 48px 0; }}
        .breadcrumb a, .breadcrumb span {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--blue-light); text-decoration: none; letter-spacing: 1px; }}
        .breadcrumb span.sep {{ margin: 0 8px; opacity: 0.4; }}
        .breadcrumb span.current {{ color: var(--text-light-muted); }}
        .blog-hero {{ background: var(--navy-deep); color: var(--text-light); padding: 24px 48px 80px; }}
        .blog-hero .inner {{ max-width: 720px; margin: 0 auto; }}
        .blog-meta {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 3px; color: var(--blue-light); margin-bottom: 20px; font-weight: 500; display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }}
        .blog-meta .reading-time {{ color: var(--text-light-muted); }}
        .blog-hero h1 {{ font-size: clamp(28px, 4vw, 40px); line-height: 1.2; margin-bottom: 24px; font-weight: 400; }}
        .blog-hero .blog-subtitle {{ font-size: 16px; line-height: 1.7; color: rgba(240, 237, 232, 0.7); max-width: 600px; }}
        .blog-content {{ max-width: 720px; margin: 0 auto; padding: 64px 48px 100px; }}
        .blog-content p {{ font-size: 16px; line-height: 1.8; color: var(--text-body); margin-bottom: 24px; }}
        .blog-content h2 {{ font-size: 22px; margin-top: 56px; margin-bottom: 20px; color: var(--text-dark); font-weight: 500; }}
        .blog-content strong {{ font-weight: 600; color: var(--text-dark); }}
        .blog-content em {{ font-style: italic; color: var(--text-muted); }}
        .divider {{ border: none; margin: 56px 0; height: 3px; background: linear-gradient(90deg, var(--blue-accent) 0%, var(--ice-blue) 50%, transparent 100%); border-radius: 2px; }}
        .stat-row {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 40px 0; }}
        .stat-box {{ background: var(--ice); border-radius: 8px; padding: 28px 20px; text-align: center; border-top: 3px solid var(--blue-accent); }}
        .stat-box .num {{ font-family: 'IBM Plex Mono', monospace; font-size: 32px; font-weight: 500; color: var(--blue-accent); display: block; margin-bottom: 4px; }}
        .stat-box .label {{ font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1.2px; font-weight: 500; }}
        .pull-quote {{ border-left: 4px solid var(--blue-accent); background: var(--ice); padding: 28px 32px; margin: 40px 0; border-radius: 0 8px 8px 0; }}
        .pull-quote p {{ font-size: 18px; font-weight: 500; color: var(--navy); margin: 0; line-height: 1.5; }}
        .pull-quote .cite {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 12px; display: block; }}
        .ba-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 40px 0; }}
        .ba-card {{ border-radius: 8px; padding: 28px 24px; }}
        .ba-card.before {{ background: var(--navy-deep); color: var(--text-light); }}
        .ba-card.after {{ background: var(--ice); color: var(--text-dark); border: 2px solid var(--blue-accent); }}
        .ba-card .ba-label {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
        .ba-card.before .ba-label {{ color: var(--red-soft); }}
        .ba-card.after .ba-label {{ color: var(--green-soft); }}
        .ba-card .ba-dot {{ width: 8px; height: 8px; border-radius: 50%; display: inline-block; }}
        .ba-card.before .ba-dot {{ background: var(--red-soft); }}
        .ba-card.after .ba-dot {{ background: var(--green-soft); }}
        .ba-card ul {{ list-style: none; padding: 0; }}
        .ba-card ul li {{ font-size: 14px; padding: 8px 0; border-bottom: 1px solid rgba(255,255,255,0.08); line-height: 1.5; }}
        .ba-card.after ul li {{ border-bottom: 1px solid var(--ice-blue); }}
        .ba-card ul li:last-child {{ border-bottom: none; }}
        .ba-card.before ul li {{ color: rgba(240, 237, 232, 0.8); }}
        .callout {{ background: var(--cream); border-radius: 8px; padding: 24px 28px; margin: 32px 0; display: flex; gap: 16px; align-items: flex-start; }}
        .callout-icon {{ font-size: 20px; flex-shrink: 0; margin-top: 2px; }}
        .callout p {{ margin: 0; font-size: 14px; line-height: 1.7; color: var(--text-body); }}
        .callout strong {{ color: var(--text-dark); }}
        .timeline {{ margin: 40px 0; padding: 0; }}
        .tl-step {{ display: flex; gap: 20px; margin-bottom: 0; position: relative; }}
        .tl-marker {{ display: flex; flex-direction: column; align-items: center; flex-shrink: 0; }}
        .tl-dot {{ width: 36px; height: 36px; border-radius: 50%; background: var(--navy-deep); color: var(--text-light); display: flex; align-items: center; justify-content: center; font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 500; }}
        .tl-line {{ width: 2px; flex-grow: 1; background: var(--ice-blue); min-height: 24px; }}
        .tl-content {{ padding: 6px 0 32px; }}
        .tl-content h4 {{ font-size: 15px; font-weight: 600; margin-bottom: 4px; color: var(--text-dark); }}
        .tl-content p {{ font-size: 14px; color: var(--text-muted); margin: 0; line-height: 1.6; }}
        .tl-step:last-child .tl-line {{ display: none; }}
        .tl-step:last-child .tl-content {{ padding-bottom: 0; }}
        .data-table {{ width: 100%; border-collapse: collapse; margin: 32px 0; font-size: 14px; border-radius: 8px; overflow: hidden; }}
        .data-table th {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--text-light); text-align: left; padding: 14px 16px; background: var(--navy-deep); font-weight: 500; }}
        .data-table td {{ padding: 12px 16px; border-bottom: 1px solid var(--ice); color: var(--text-body); }}
        .data-table tr:last-child td {{ border-bottom: none; }}
        .data-table tr:nth-child(even) {{ background: var(--ice); }}
        .pipeline-wrap {{ background: var(--navy-deep); border-radius: 12px; padding: 32px; margin: 40px 0; overflow-x: auto; }}
        .pipeline-label {{ font-family: 'IBM Plex Mono', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: var(--blue-light); margin-bottom: 16px; }}
        .pipeline-flow {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }}
        .pipeline-stage {{ font-family: 'IBM Plex Mono', monospace; font-size: 10px; background: var(--navy-mid); color: var(--text-light); padding: 8px 12px; border-radius: 4px; white-space: nowrap; border: 1px solid rgba(74, 143, 212, 0.2); }}
        .pipeline-arrow {{ color: var(--blue-accent); font-size: 12px; }}
        .faq-section {{ margin-top: 56px; }}
        .faq-item {{ border-bottom: 1px solid var(--ice-blue); padding: 20px 0; }}
        .faq-q {{ font-size: 15px; font-weight: 600; color: var(--text-dark); cursor: pointer; display: flex; justify-content: space-between; align-items: center; }}
        .faq-q::after {{ content: '+'; font-family: 'IBM Plex Mono', monospace; font-size: 18px; color: var(--blue-accent); transition: transform 0.2s; }}
        .faq-item.open .faq-q::after {{ content: '\\2212'; }}
        .faq-a {{ font-size: 14px; color: var(--text-body); line-height: 1.7; padding-top: 12px; display: none; }}
        .faq-item.open .faq-a {{ display: block; }}
        .author-card {{ display: flex; gap: 20px; align-items: center; background: var(--ice); border-radius: 12px; padding: 28px; margin-top: 48px; }}
        .author-avatar {{ width: 64px; height: 64px; border-radius: 50%; background: var(--navy-deep); color: var(--blue-accent); display: flex; align-items: center; justify-content: center; font-family: 'IBM Plex Mono', monospace; font-size: 20px; font-weight: 600; flex-shrink: 0; }}
        .author-info h4 {{ font-size: 15px; font-weight: 600; color: var(--text-dark); margin-bottom: 4px; }}
        .author-info p {{ font-size: 13px; color: var(--text-muted); margin: 0; line-height: 1.6; }}
        .author-info a {{ color: var(--blue-accent); text-decoration: none; font-weight: 500; }}
        .blog-cta {{ background: var(--navy-deep); border-radius: 12px; padding: 48px 40px; margin: 56px 0 0; text-align: center; }}
        .blog-cta h3 {{ color: var(--text-light); font-size: 22px; font-weight: 400; margin-bottom: 12px; }}
        .blog-cta p {{ color: rgba(240, 237, 232, 0.7); font-size: 15px; margin-bottom: 28px; }}
        .btn-primary {{ font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: 1.5px; color: var(--navy-deep); background: var(--blue-accent); padding: 14px 32px; border-radius: 4px; text-decoration: none; transition: all 0.3s; display: inline-block; }}
        .btn-primary:hover {{ background: var(--blue-light); }}
        .footer {{ background: var(--navy-deep); padding: 32px 48px; border-top: 1px solid rgba(255,255,255,0.06); }}
        .footer-inner {{ max-width: 960px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }}
        .footer-inner p {{ font-size: 13px; color: var(--text-light-muted); }}
        .footer-inner a {{ font-size: 13px; color: var(--text-light-muted); text-decoration: none; }}
        .footer-inner a:hover {{ color: var(--text-light); }}
        @media (max-width: 768px) {{
            nav {{ padding: 16px 24px; }}
            .breadcrumb {{ padding: 100px 24px 0; }}
            .blog-hero {{ padding: 24px 24px 60px; }}
            .blog-content {{ padding: 48px 24px 80px; }}
            .stat-row {{ grid-template-columns: 1fr; }}
            .ba-grid {{ grid-template-columns: 1fr; }}
            .pipeline-wrap {{ padding: 20px; }}
            .pipeline-flow {{ flex-direction: column; }}
            .pipeline-arrow {{ transform: rotate(90deg); }}
            .author-card {{ flex-direction: column; text-align: center; }}
            .footer {{ padding: 24px; }}
        }}
    </style>
</head>
<body>

    <nav>
        <a href="/" class="logo">Formaum</a>
        <div class="nav-right">
            <a href="/" class="nav-link">Home</a>
            <a href="/blog/" class="nav-link">Blog</a>
            <a href="https://cal.com/formaum/45" class="nav-cta" target="_blank">Book a Call</a>
        </div>
    </nav>

    <div class="blog-hero">
        <div class="breadcrumb">
            <a href="/">Home</a><span class="sep">/</span>
            <a href="/blog/">Blog</a><span class="sep">/</span>
            <span class="current">{breadcrumb_label}</span>
        </div>
        <div class="inner" style="padding-top: 32px;">
            <div class="blog-meta">
                <span>{blog_label}</span>
                <span class="reading-time">{reading_time}</span>
            </div>
            <h1>{title}</h1>
            <p class="blog-subtitle">{subtitle}</p>
        </div>
    </div>

    <div class="blog-content">

{content_html}

{faq_html}

        <div class="blog-cta">
            <h3>Running on a stack that grew by accident?</h3>
            <p>Tools added one at a time, never architected together. That's the problem I solve. Book 45 minutes and I'll map what moves, what stays, and what makes sense for your operation.</p>
            <a href="https://cal.com/formaum/45" class="btn-primary" target="_blank">Book a Discovery Call</a>
        </div>

        <div class="author-card">
            <div class="author-avatar">GC</div>
            <div class="author-info">
                <h4>Genevieve Claire</h4>
                <p>Operations strategist. Previously EA Sports FIFA &mdash; $100M productions, $7B franchise. Now I build operations infrastructure for multi-location businesses. <a href="https://linkedin.com/in/genevieveclaire" target="_blank">LinkedIn &rarr;</a></p>
            </div>
        </div>

    </div>

    <div class="footer">
        <div class="footer-inner">
            <p>&copy; 2026 Formaum, Inc.</p>
            <a href="https://linkedin.com/in/genevieveclaire" target="_blank">LinkedIn</a>
        </div>
    </div>

    <script>
        document.querySelectorAll('.faq-q').forEach(q => {{
            q.addEventListener('click', () => {{
                q.parentElement.classList.toggle('open');
            }});
        }});
    </script>

</body>
</html>'''

    outpath = os.path.join(os.path.dirname(__file__), f"{slug}.html")
    with open(outpath, "w") as f:
        f.write(html)
    print(f"Built: {outpath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 build.py config.json")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        config = json.load(f)
    build(config)
