from typing import Dict, List, Any
from enum import Enum
import pdfrw
from pdfrw import PdfName
import json


class Role(str, Enum):
    """Possible "/FT" field values.

    See https://web.archive.org/web/20220404024706/https://www.w3.org/TR/WCAG20-TECHS/PDF12.html
    """

    TEXT = PdfName("Tx")
    BUTTON = PdfName("Btn")  # Also captures checkbox and radio button
    COMBO_BOX = PdfName("Ch")  # Also captures list box
    SIGNATURE = PdfName("Sig")

    def has_item(cls, item):
        # https://stackoverflow.com/questions/43634618/how-do-i-test-if-int-value-exists-in-python-enum-without-using-try-catch
        try:
            cls(item)
        except ValueError:
            return False
        else:
            return True

    @classmethod
    def values(cls):
        return [value.value for value in cls]


class ButtonVal(str, Enum):
    """Possible "/V" and "/AS" values for a Role.BUTTON field."""

    OFF = PdfName("Off")
    ON = PdfName("On")

    @classmethod
    def has_item(cls, item):
        # https://stackoverflow.com/questions/43634618/how-do-i-test-if-int-value-exists-in-python-enum-without-using-try-catch
        try:
            cls(item)
        except ValueError:
            return False
        else:
            return True

    @classmethod
    def values(cls):
        return [value.value for value in cls]


class Pdf:
    """Pdf reads fillable pdfs and offers functions to fill them in.

    Args:
        path (str): The fillable pdf's path. This object will read in the
            pdf stored at that path. It will not modify that pdf.

    Raises:
        ValueError: If the pdf has fillable fields with duplicate names.
    """

    def __init__(self, path: str):
        self.path: str = path
        self.reader: pdfrw.PdfReader = pdfrw.PdfReader(path)
        self.annots: Dict = self._parse_fillable_annotations()

    def is_fillable_annotation(self, annotation: Dict):
        """Check whether the annotation is fillable."""

        return (annotation.get("/Subtype") == "/Widget"
                and "/T" in annotation
                and "/FT" in annotation)

    def fill(self, annotation: Dict, value: str) -> None:
        """Fills a fillable annotation.

        Raises:
            ValueError: If the annotation has an unexpected format or the role
                is invalid.
            NotImplementedError: If the annotation's role has not been
                implemented.
        """

        if PdfName("FT") not in annotation:
            raise ValueError(f"No \"{PdfName('FT')}\" key found in annotation. "
                             "Annotation must contain an \"FT\" key with one "
                             f"of the following values: {', '.join(Role.values())}."
                             f"\nAnnotation data received: {annotation}")

        role = annotation["/FT"]

        if role == Role.TEXT:
            annotation.update(pdfrw.PdfDict(AP=value, V=value))
        elif role == Role.BUTTON:
            if not ButtonVal.has_item(PdfName(value)):
                raise ValueError(f"Got unexpected raw value \"{value}\" for button "
                                 f"\"{annotation['/T']}\". The value's PdfName "
                                 f"was \"{PdfName(value)}\". A button's value "
                                 "must have one of the following PdfNames: "
                                 f"{', '.join(ButtonVal.values())}.")
            annotation.update(pdfrw.PdfDict(
                AS=PdfName(value), V=PdfName(value)))
        elif role == Role.COMBO_BOX:
            raise NotImplementedError("Combo boxes and list boxes are "
                                      "currently unsupported.")
        elif role == Role.SIGNATURE:
            raise NotImplementedError("Signatures are currently unsupported.")
        else:
            raise ValueError("Got unexpected role (\"FT\") value of "
                             f"\"{role}\". Role must be on of the following "
                             f"values: {', '.join(Role.values())}.")

    def bulk_fill(self, values: List[Any]):
        if len(values) != len(self.annots):
            raise ValueError("Got values list with unexpected length "
                             f"{len(values)}. Expected {len(self.annots)} "
                             "values, equal to the number of annotations.")

        for annot, value in zip(self.annots, values):
            self.fill(annot, value)

    def key_fill(self, key: str, value: str):
        for annot in self.annots:
            if annot['/T'] == f"({key})":
                self.fill(annot, value)

    def save(self, output_path: str):
        """Saves this pdf, including filled-in fields, at the output_path."""

        self.reader.Root.AcroForm.update(
            pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject("true"))
        )
        pdfrw.PdfWriter().write(output_path, self.reader)

    def dumps(self) -> str:
        return json.dumps(self.to_list())

    def to_list(self) -> List:
        return [self.annotation_to_dict(annot, idx) for idx, annot in enumerate(self.annots)]

    @staticmethod
    def annotation_to_dict(annot, idx=0) -> Dict:
        return {
            "T": annot[PdfName("T")],
            "FT": annot[PdfName("FT")],
            "Rect": annot[PdfName("Rect")],
            "idx": idx,
        }

    def _parse_fillable_annotations(self) -> Dict:
        fillable_annots = []

        for p in self.reader.pages:
            annotations = p["/Annots"]
            if annotations is None:
                continue

            for a in annotations:
                if self.is_fillable_annotation(a):
                    fillable_annots.append(a)

        return fillable_annots
