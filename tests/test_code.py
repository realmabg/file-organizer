from organizer import organize_by_type
from organizer import organize_by_keyword

def test_function_exists():
    assert callable(organize_by_type)

def test_pdf_moves_to_pdf_folder(tmp_path):
    pdf = tmp_path / "resume.pdf"
    pdf.write_text("test")

    organize_by_type(tmp_path)

    assert (tmp_path / "pdf" / "resume.pdf").exists()

def test_file_without_extension(tmp_path):
    file = tmp_path / "README"
    file.write_text("hello")

    organize_by_type(tmp_path)

    assert (tmp_path / "no_extension" / "README").exists()



def test_keyword_moves_matching_file(tmp_path):
    file = tmp_path / "school_notes.txt"
    file.write_text("notes")

    organize_by_keyword(tmp_path, "school")

    assert (tmp_path / "school" / "school_notes.txt").exists()

def test_keyword_does_not_move_nonmatching_file(tmp_path):
    file = tmp_path / "vacation.jpg"
    file.write_text("photo")

    organize_by_keyword(tmp_path, "school")

    assert file.exists()


from organizer import organize_by_type

def test_invalid_folder(capsys):
    organize_by_type("this_folder_does_not_exist")

    captured = capsys.readouterr()

    assert "Folder does not exist." in captured.out

from organizer import organize_by_type

def test_empty_folder(tmp_path, capsys):
    organize_by_type(tmp_path)

    captured = capsys.readouterr()

    assert "Folder contains no files." in captured.out

from organizer import organize_by_type

def test_unsupported_file_type(tmp_path, capsys):
    file = tmp_path / "virus.exe"
    file.write_text("test")

    organize_by_type(tmp_path)

    captured = capsys.readouterr()

    assert "Unsupported file type: exe" in captured.out

from organizer import organize_by_keyword

def test_keyword_not_found(tmp_path, capsys):
    file = tmp_path / "vacation.jpg"
    file.write_text("test")

    organize_by_keyword(tmp_path, "school")

    captured = capsys.readouterr()

    assert "No files matched that keyword." in captured.out

from organizer import organize_by_type

def test_duplicate_file(tmp_path, capsys):
    source = tmp_path / "resume.pdf"
    source.write_text("original")

    pdf_folder = tmp_path / "pdf"
    pdf_folder.mkdir()

    duplicate = pdf_folder / "resume.pdf"
    duplicate.write_text("duplicate")

    organize_by_type(tmp_path)

    captured = capsys.readouterr()

    assert "Skipping resume.pdf" in captured.out