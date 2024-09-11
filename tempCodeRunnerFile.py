from fpdf import FPDF
import os

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, txt="IBRAHIM AMR", ln=True, align="C")
pdf.cell(200, 10, txt="Software Engineer", ln=True, align="C")

# Contact Information
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Cairo, Egypt | ibrahim.amr775@gmail.com | 01125700310", ln=True, align="C")

# Add LinkedIn link
pdf.set_font("Arial", size=12)
linkedin_url = "https://www.linkedin.com/in/ibrahim-amr-b238bb316?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app"
pdf.cell(200, 10, txt="LinkedIn: linkedin.com/in/ibrahim-amr", ln=True, align="C", link=linkedin_url)

# Add separator line
pdf.ln(10)  # Line break
pdf.ln(10)  # Line break

# Add section: Education
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt="Education", ln=True)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw line

pdf.set_font("Arial", size=12)
pdf.cell(0, 10, txt="Helwan University - Faculty of Computer Science and Artificial Intelligence", ln=True)
pdf.cell(0, 10, txt="Bachelor's in Computer Science", ln=True)
pdf.cell(0, 10, txt="2022 - 2026 (Expected)", ln=True, align="R")
pdf.ln(5)  # Line break

# Add section: Skills
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt="Skills", ln=True)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw line

pdf.set_font("Arial", size=14)
skills = """
* Front-end Web Development 
* UI & UX Design
* Software Testing
* SOLID Principles
* Problem Solving (Python, OOP)
* Version Control (Git & GitHub)
* SDLC (Software Development Life Cycle)
* Agile & Waterfall Methodologies
* Database Management (SQL, MySQL)
* UML Diagrams
* Teamwork and Leadership
* Time Management
* Communication & Presentation Skills
"""
pdf.multi_cell(0, 10, txt=skills)
pdf.ln(10)  # Line break

# Add section: Experience
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt="Experience", ln=True)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw line

pdf.set_font("Arial", size=12)
experience = """
Instructor and Course Supervisor                 2024
* Led a course covering UI/UX, software fundamentals, Agile methodologies, requirements, design patterns, SOLID principles, software testing, and SQL/MySQL.
* Developed curriculum and provided hands-on training to students.

Teaching and Training                            2023 - 2025
* Acted as a lecturer for practical and theoretical courses in the Computer Science department.
"""
pdf.multi_cell(0, 10, txt=experience)
pdf.ln(10)  # Line break

# Add section: Projects
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt="Projects", ln=True)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw line

pdf.set_font("Arial", size=12)
projects = """
Gaming and E-sports Website                       2024
* Designed and developed a website for organizing gaming events and e-sports tournaments.
* The platform allowed users to register for online tournaments and gaming events.
* Managed project tasks using UML diagrams to plan the architecture and workflows.
* Utilized HTML, CSS, and JavaScript to build an interactive and responsive user interface.
* Ensured optimal performance and user experience, particularly for live event scheduling.
* GitHub: https://github.com/XZBM7/GAME_7

E-commerce Website                                2023 - 2024
* Led a team to design an online store for selling products.
* Utilized HTML, CSS, and JS for front-end development.
* Managed the project timeline, assigned tasks, and ensured optimal user experience.
* GitHub: https://github.com/XZBM7/Z-SHOP

Social Media Website                              2023 - 2024
* Designed a social media platform for sharing photos and videos, similar to Instagram.
* Led a team that divided tasks and followed a strict plan using UML diagrams.
* Built key UML diagrams such as Class diagrams and design structures.
* Developed the user interface using HTML, CSS, JS, and Bootstrap.
* Achieved maximum performance as planned for the application.
* GitHub: (To be added if available)

AI-based Game                                     2024
* Developed a 2D game using Python and Pygame library where an AI character chases the player.
* The player collects points to win, and the game features a two-player mode where friends can compete.
* Integrated a settings menu allowing players to customize game difficulty and appearance.
* Implemented a database system using the JSON library to save and load player statistics and performance.
* Created the game's architecture with UML diagrams, ensuring smooth and efficient development.
* GitHub: https://github.com/XZBM7/python-game-pec-man
"""
pdf.multi_cell(0, 10, txt=projects)
pdf.ln(10)  # Line break

# Add section: Languages
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt="Languages", ln=True)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw line

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="* Arabic: Native\n* English: Good")
pdf.ln(10)  # Line break

# Add section: Contact
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt="Contact", ln=True)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw line

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="Email: ibrahim.amr775@gmail.com\nPhone: 01125700310\nLocation: 36 Saleh Hijazi Street, Maadi, Cairo")

# Save the PDF to a valid file location
pdf_output = "C:/Users/HUAWEI/Documents/Ibrahim_Amr_CV.pdf"  # Save it in the Documents folder
pdf.output(pdf_output)

print(f"PDF saved successfully as {pdf_output}")

# Open the PDF file
os.startfile(pdf_output)  # This method works on Windows
