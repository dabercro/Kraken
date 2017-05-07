#!/bin/bash
BASE_SE=/cms/store/user/paus
CATALOG=/home/cmsprod/catalog/t2mit

CFG="pandaf"
VRS="003"

BOOK_SRC="$CFG/$VRS"
BOOK_TGT="$CFG/x03"

FILE="$1"
if ! [ -e "$FILE" ]
then
  echo ""
  echo " ERROR file: $FILE does not exist."
  echo ""
  exit 1
fi

# make the relevant directories
makedir  $BASE_SE/$BOOK_TGT
mkdir -p $CATALOG/$BOOK_TGT

for sample in `cat "$FILE"`
do
  echo "=@=@=@=@= $sample"
  echo ""

  # move sample catalog
  mv   $CATALOG/$BOOK_SRC/$sample $CATALOG/$BOOK_TGT/$sample
  repstr $BOOK_SRC $BOOK_TGT $CATALOG/$BOOK_TGT/$sample/*

  # move sample physically
  t2tools.py --action=mv --source=$BASE_SE/$BOOK_SRC/$sample --target=$BASE_SE/$BOOK_TGT/$sample

  # remove catalog entries
  removeData.py --config=$CFG --version=$VRS --dataset=$sample --py=mc --exec
  echo ""
  
done
