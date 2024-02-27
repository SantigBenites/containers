import os, shutil, subprocess

# Intruduce Acronym
ACRONYM = "BI"

# Consts
CURRENT_DIR = os.getcwd()
TEMPLATE_DIR = f"{CURRENT_DIR}/classes/template"


# Copy template to new container directory
try:
    shutil.copytree(TEMPLATE_DIR, f"{CURRENT_DIR}/classes/{ACRONYM}")
except Exception:
    pass


# Make icon
subprocess.check_call(f"{CURRENT_DIR}/classes/utils/gen_cli_icon.sh %s %s" % (ACRONYM, f"{CURRENT_DIR}/classes/{ACRONYM}/{ACRONYM}.png"), shell=True)

