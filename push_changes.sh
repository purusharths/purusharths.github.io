#!/bin/bash

# Optional commit message
msg="$1"
if [ -z "$msg" ]; then
  msg="Blog update: $(date)"
fi

# Step 1: Build the site
echo "Building site with 'make html'..."
make html

# Step 2: Stage changes
echo "Staging content and output..."
git add content/posts/
git add output/

# Step 3: Commit
echo "Committing..."
git commit -m "$msg"

# Step 4: Push
echo "Pushing to GitHub..."
git push

echo "Done."
