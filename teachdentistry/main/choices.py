AGE_CHOICES = (
    ('-----', '-----'),
    ('G1', 'Under 20'),
    ('G2', '20-29'),
    ('G3', '30-39'),
    ('G4', '40-49'),
    ('G5', '50-59'),
    ('G6', '60-69'),
    ('G7', '70 or older'),
)

AGREEMENT_CHOICES = (
    ('-----', '-----'),
    ('A1', 'Strongly agree'),
    ('A2', 'Agree'),
    ('A3', 'Neutral'),
    ('A4', 'Disagree'),
    ('A5', 'Strongly disagree')
)

AGREEMENT_CHOICES_EX = (
    ('-----', '-----'),
    ('A1', 'Strongly agree'),
    ('A2', 'Agree'),
    ('A3', 'Neutral'),
    ('A4', 'Disagree'),
    ('A5', 'Strongly disagree'),
    ('A6', "I don't know the benefits"),
    ('A7', "I don't know the challenges"),
    ('A8', "I don't know the benefits or the challenges")
)

CONSENT_CHOICES = (
    ('C0', 'Have not consented'),
    ('C1', 'Consented')
)

CAREER_STAGE_CHOICES = (
    ('E', 'Early career'),
    ('M', 'Mid career'),
    ('L', 'Late career')
)

DEGREE_CHOICES = (
    ('-----', '-----'),
    ('D1', 'High School diploma/GED'),
    ('D2', 'Associate Degree or Equivalent'),
    ('D3', "Bachelor's Degree or Equivalent"),
    ('D4', "Master's Degree"),
    ('D5', 'DDS or DMD'),
    ('D6', 'MD'),
    ('D7', 'PhD'),
    ('D8', 'Other Doctorate'),
)

DISCIPLINE_CHOICES = (
    ('-----', '-----'),
    ('S1', 'Dentistry, general'),
    ('S2', 'Dentistry, pediatric'),
    ('S3', 'Dentistry, public health'),
    ('S4', 'Dentistry, Other'),
    ('S5', 'Other'),
)

ETHNICITY_CHOICES = (
    ('-----', '-----'),
    ('E1', 'Hispanic or Latino'),
    ('E2', 'Non-Hispanic or Non-Latino')
)

RACE_CHOICES = (
    ('R1', 'Black/African American'),
    ('R2', 'White'),
    ('R3', 'Native Hawaiian or Other Pacific Islander'),
    ('R4', 'Asian'),
    ('R5', 'American Indian/Alaska Native'),
    ('R6', 'Other')
)

RACE_CHOICES_EX = (
    ('-----', '-----'),
    ('R1', 'American Indian or Alaska Native'),
    ('R2', 'Chinese, Filipino, Japanese, Korean, Asian Indian, or Thai'),
    ('R3', 'Other Asian'),
    ('R4', 'Black or African American'),
    ('R5', 'Native Hawaiian or other Pacific Islander'),
    ('R6', 'White'),
)

GENDER_CHOICES = (
    ('-----', '-----'),
    ('M', 'Male'),
    ('F', 'Female')
)

WORK_CHOICES = (
    ('C1', 'Clinical practice, Full-time private practice'),
    ('C2', 'Clinical practice, Part-time private practice'),
    ('C3', 'Clinical practice, Full-time safety net practice'),
    ('C4', 'Clinical practice, Part-time safety net practice'),
    ('C5', """Non-clinical practice: Full time in academia
        (includes teaching and research, advocacy, and the public sector)"""),
    ('C6', """Non-clinical practice: Part time in academia
        (includes teaching and research, advocacy and
        the public health sector)"""),
    ('C7', """Non-clinical practice: Full time in
        the corporate sector"""),
    ('C8', """Non-clinical practice: Part time in the
        corporate sector"""),
)

DENTAL_SCHOOL_CHOICES = (
    ("-----", "-----"),
    ("A.T. Still University Arizona School of Dentistry and Oral Health",
     "A.T. Still University Arizona School of Dentistry and Oral Health"),
    ("Baylor College of Dentistry Component of Texas A &amp; M Health Sci Ctr",
     """Baylor College of Dentistry Component of Texas A &amp; M
     Health Sci Ctr"""),
    ("Boston University Goldman School of Dental Medicine",
     "Boston University Goldman School of Dental Medicine"),
    ("Case Western Reserve Univ. School of Dental Medicine",
     "Case Western Reserve Univ. School of Dental Medicine"),
    ("Columbia University College of Dental Medicine",
     "Columbia University College of Dental Medicine"),
    ("Creighton University School of Dentistry",
     "Creighton University School of Dentistry"),
    ("East Carolina University School of Dental Medicine",
     "East Carolina University School of Dental Medicine"),
    ("Georgia Health Sciences University School of Dentistry",
     "Georgia Health Sciences University School of Dentistry"),
    ("Harvard University School of Dental Medicine",
     "Harvard University School of Dental Medicine"),
    ("Herman Ostrow School of Dentistry of USC",
     "Herman Ostrow School of Dentistry of USC"),
    ("Howard University College of Dentistry",
     "Howard University College of Dentistry"),
    ("Indiana University School of Dentistry",
     "Indiana University School of Dentistry"),
    ("LECOM College of Dental Medicine",
     "LECOM College of Dental Medicine"),
    ("Loma Linda University School of Dentistry",
     "Loma Linda University School of Dentistry"),
    ("Louisiana State University School of Dentistry",
     "Louisiana State University School of Dentistry"),
    ("Marquette University School of Dentistry",
     "Marquette University School of Dentistry"),
    ("""Medical University of South Carolina James B.
        Edwards College of Dental Medicine""",
     """Medical University of South Carolina James B.
         Edwards College of Dental Medicine"""),
    ("Meharry Medical College School of Dentistry",
     "Meharry Medical College School of Dentistry"),
    ("Midwestern University College of Dental Medicine - Arizona",
     "Midwestern University College of Dental Medicine- Arizona"),
    ("Midwestern University College of Dental Medicine- Illinois",
     "Midwestern University College of Dental Medicine - Illinois"),
    ("New York University College of Dentistry",
     "New York University College of Dentistry"),
    ("Nova Southeastern University College of Dental Medicine",
     "Nova Southeastern University College of Dental Medicine"),
    ("Ohio State University College of Dentistry",
     "Ohio State University College of Dentistry"),
    ("Oregon Health and Science University School of Dentistry",
     "Oregon Health and Science University School of Dentistry"),
    ("Southern Illinois University School of Dental Medicine",
     "Southern Illinois University School of Dental Medicine"),
    ("State University of New York at Buffalo School of Dental Medicine",
     "State University of New York at Buffalo School of Dental Medicine"),
    ("State University of New York at Stony Brook School of Dental Medicine",
     "State University of New York at Stony Brook School of Dental Medicine"),
    ("Temple University The Maurice H. Kornberg School of Dentistry",
     "Temple University The Maurice H. Kornberg School of Dentistry"),
    ("Tufts University School of Dental Medicine",
     "Tufts University School of Dental Medicine"),
    ("University of Alabama School of Dentistry at UAB",
     "University of Alabama School of Dentistry at UAB"),
    ("University of California at Los Angeles School of Dentistry",
     "University of California at Los Angeles School of Dentistry"),
    ("University of California at San Francisco School of Dentistry",
     "University of California at San Francisco School of Dentistry"),
    ("University of Colorado Denver",
     "University of Colorado Denver"),
    ("University of Connecticut School of Dental Medicine",
     "University of Connecticut School of Dental Medicine"),
    ("University of Detroit Mercy School of Dentistry",
     "University of Detroit Mercy School of Dentistry"),
    ("University of Florida College of Dentistry",
     "University of Florida College of Dentistry"),
    ("University of Illinois at Chicago College of Dentistry",
     "University of Illinois at Chicago College of Dentistry"),
    ("University of Iowa College of Dentistry",
     "University of Iowa College of Dentistry"),
    ("University of Kentucky College of Dentistry",
     "University of Kentucky College of Dentistry"),
    ("University of Louisville School of Dentistry",
     "University of Louisville School of Dentistry"),
    ("University of Maryland Baltimore College of Dental Surgery",
     "University of Maryland Baltimore College of Dental Surgery"),
    ("""University of Medicine &amp; Dentistry of
    New Jersey New Jersey Dental School""",
     """University of Medicine &amp; Dentistry of
        New Jersey New Jersey Dental School"""),
    ("University of Michigan School of Dentistry",
     "University of Michigan School of Dentistry"),
    ("University of Minnesota School of Dentistry",
     "University of Minnesota School of Dentistry"),
    ("University of Mississippi School of Dentistry",
     "University of Mississippi School of Dentistry"),
    ("University of Missouri - Kansas City School of Dentistry",
     "University of Missouri-Kansas City School of Dentistry"),
    ("University of Nebraska Medical Center College of Dentistry",
     "University of Nebraska Medical Center College of Dentistry"),
    ("University of Nevada Las Vegas School of Dental Medicine",
     "University of Nevada Las Vegas School of Dental Medicine"),
    ("University of North Carolina School of Dentistry",
     "University of North Carolina School of Dentistry"),
    ("University of Oklahoma College of Dentistry",
     "University of Oklahoma College of Dentistry"),
    ("University of Pennsylvania School of Dental Medicine",
     "University of Pennsylvania School of Dental Medicine"),
    ("University of Pittsburgh School of Dental Medicine",
     "University of Pittsburgh School of Dental Medicine"),
    ("University of Puerto Rico School of Dental Medicine",
     "University of Puerto Rico School of Dental Medicine"),
    ("University of Tennessee College of Dentistry",
     "University of Tennessee College of Dentistry"),
    ("University of Texas Hlth Science Cnt-San Antonio Dental School",
     "University of Texas Hlth Science Cnt - San Antonio Dental School"),
    ("University of Texas School of Dentistry at Houston",
     "University of Texas School of Dentistry at Houston"),
    ("University of the Pacific Arthur A. Dugoni School of Dentistry",
     "University of the Pacific Arthur A. Dugoni School of Dentistry"),
    ("University of Washington-Health Sciences School of Dentistry",
     "University of Washington-Health Sciences School of Dentistry"),
    ("Virginia Commonwealth University School of Dentistry",
     "Virginia Commonwealth University School of Dentistry"),
    ("West Virginia University School of Dentistry",
     "West Virginia University School of Dentistry"),
    ("Western University of Health Sciences College of Dental Medicine",
     "Western University of Health Sciences College of Dental Medicine"),
    ("Other", "Other")
)
