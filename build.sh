echo "Removing dist and build directories..."
rm -rf build/ dist/

echo "Building..."
python3 -m build

echo "Checking build..."
twine check dist/*

twine upload dist/*