import os

import pytest

from file_organizer.organizer import organizer, preview


@pytest.mark.parametrize(
    ("filename", "category"),
    [
        ("photo.jpg", "Images"),
        ("photo.jpeg", "Images"),
        ("photo.png", "Images"),
        ("photo.gif", "Images"),
        ("song.mp3", "Music"),
        ("song.flac", "Music"),
        ("song.wav", "Music"),
        ("song.m4a", "Music"),
        ("movie.mp4", "Videos"),
        ("movie.mkv", "Videos"),
        ("movie.avi", "Videos"),
        ("document.pdf", "Documents"),
        ("document.docx", "Documents"),
        ("document.txt", "Documents"),
        ("archive.zip", "Archives"),
        ("archive.7z", "Archives"),
        ("archive.rar", "Archives"),
        ("script.py", "Code"),
        ("page.html", "Code"),
        ("program.cpp", "Code"),
        ("package.deb", "Packages"),
        ("installer.run", "Packages"),
    ],
)
def test_file_is_organized_into_correct_category(
    tmp_path,
    filename,
    category,
):
    file = tmp_path / filename
    file.write_text("test")

    total, moved, failed, success = organizer(str(tmp_path))

    assert total == 1
    assert moved == 1
    assert failed == 0
    assert success is True
    assert (tmp_path / category / filename).exists()


def test_organizes_image(tmp_path):
    file = tmp_path / "photo.jpg"
    file.write_text("image")

    total, moved, failed, success = organizer(str(tmp_path))

    assert total == 1
    assert moved == 1
    assert failed == 0
    assert success is True
    assert (tmp_path / "Images" / "photo.jpg").exists()


def test_organizes_music(tmp_path):
    file = tmp_path / "song.mp3"
    file.write_text("music")

    total, moved, failed, success = organizer(str(tmp_path))

    assert total == 1
    assert moved == 1
    assert failed == 0
    assert success is True
    assert (tmp_path / "Music" / "song.mp3").exists()


def test_organizes_video(tmp_path):
    file = tmp_path / "movie.mp4"
    file.write_text("video")

    organizer(str(tmp_path))

    assert (tmp_path / "Videos" / "movie.mp4").exists()


def test_organizes_document(tmp_path):
    file = tmp_path / "document.pdf"
    file.write_text("document")

    organizer(str(tmp_path))

    assert (tmp_path / "Documents" / "document.pdf").exists()


def test_organizes_archive(tmp_path):
    file = tmp_path / "archive.zip"
    file.write_text("archive")

    organizer(str(tmp_path))

    assert (tmp_path / "Archives" / "archive.zip").exists()


def test_organizes_code(tmp_path):
    file = tmp_path / "script.py"
    file.write_text("print('hello')")

    organizer(str(tmp_path))

    assert (tmp_path / "Code" / "script.py").exists()


def test_organizes_package(tmp_path):
    file = tmp_path / "program.deb"
    file.write_text("package")

    organizer(str(tmp_path))

    assert (tmp_path / "Packages" / "program.deb").exists()


def test_unknown_extension_goes_to_other(tmp_path):
    file = tmp_path / "something.xyz"
    file.write_text("unknown")

    organizer(str(tmp_path))

    assert (tmp_path / "Other" / "something.xyz").exists()


def test_uppercase_extension(tmp_path):
    file = tmp_path / "PHOTO.JPG"
    file.write_text("image")

    organizer(str(tmp_path))

    assert (tmp_path / "Images" / "PHOTO.JPG").exists()


def test_file_is_moved(tmp_path):
    file = tmp_path / "photo.jpg"
    file.write_text("important content")

    organizer(str(tmp_path))

    assert not file.exists()

    new_file = tmp_path / "Images" / "photo.jpg"
    assert new_file.exists()
    assert new_file.read_text() == "important content"


def test_duplicate_file_is_renamed(tmp_path):
    images = tmp_path / "Images"
    images.mkdir()

    existing = images / "photo.jpg"
    existing.write_text("old")

    new_file = tmp_path / "photo.jpg"
    new_file.write_text("new")

    organizer(str(tmp_path))

    assert existing.exists()
    assert (images / "photo (1).jpg").exists()

    assert existing.read_text() == "old"
    assert (images / "photo (1).jpg").read_text() == "new"


def test_multiple_duplicates_are_renamed(tmp_path):
    images = tmp_path / "Images"
    images.mkdir()

    (images / "photo.jpg").write_text("first")
    (images / "photo (1).jpg").write_text("second")

    new_file = tmp_path / "photo.jpg"
    new_file.write_text("third")

    organizer(str(tmp_path))

    assert (images / "photo.jpg").read_text() == "first"
    assert (images / "photo (1).jpg").read_text() == "second"
    assert (images / "photo (2).jpg").read_text() == "third"


def test_empty_directory(tmp_path):
    total, moved, failed, success = organizer(str(tmp_path))

    assert total == 0
    assert moved == 0
    assert failed == 0
    assert success is True


def test_already_organized_file_is_skipped(tmp_path):
    images = tmp_path / "Images"
    images.mkdir()

    file = images / "photo.jpg"
    file.write_text("image")

    total, moved, failed, success = organizer(str(tmp_path))

    assert total == 0
    assert moved == 0
    assert failed == 0
    assert success is True
    assert file.exists()


def test_multiple_files(tmp_path):
    (tmp_path / "photo.jpg").write_text("image")
    (tmp_path / "song.mp3").write_text("music")
    (tmp_path / "movie.mp4").write_text("video")
    (tmp_path / "document.pdf").write_text("document")
    (tmp_path / "archive.zip").write_text("archive")
    (tmp_path / "script.py").write_text("code")
    (tmp_path / "program.deb").write_text("package")

    total, moved, failed, success = organizer(str(tmp_path))

    assert total == 7
    assert moved == 7
    assert failed == 0
    assert success is True

    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "Music" / "song.mp3").exists()
    assert (tmp_path / "Videos" / "movie.mp4").exists()
    assert (tmp_path / "Documents" / "document.pdf").exists()
    assert (tmp_path / "Archives" / "archive.zip").exists()
    assert (tmp_path / "Code" / "script.py").exists()
    assert (tmp_path / "Packages" / "program.deb").exists()


# --- New tests for the 4-tuple return / failure tracking ---


def test_nonexistent_path_returns_zero_and_failure(tmp_path):
    missing = tmp_path / "does_not_exist"

    total, moved, failed, success = organizer(str(missing))

    assert total == 0
    assert moved == 0
    assert failed == 0
    assert success is False


def test_path_is_a_file_not_a_directory_returns_failure(tmp_path):
    file_path = tmp_path / "not_a_folder.txt"
    file_path.write_text("i am a file")

    total, moved, failed, success = organizer(str(file_path))

    assert total == 0
    assert moved == 0
    assert failed == 0
    assert success is False


@pytest.mark.skipif(os.name == "nt", reason="chmod-based permission test is unreliable on Windows")
def test_permission_error_is_tracked_as_failed_and_continues(tmp_path):
    # One file we can move, one file whose destination folder we lock down
    # so the move fails, to confirm failures are tracked and don't stop the batch
    good_file = tmp_path / "good.jpg"
    good_file.write_text("ok")

    bad_file = tmp_path / "bad.mp3"
    bad_file.write_text("blocked")

    # Pre-create the Music destination folder as read-only so the move into it fails
    music_dir = tmp_path / "Music"
    music_dir.mkdir()
    music_dir.chmod(0o500)

    try:
        total, moved, failed, success = organizer(str(tmp_path))

        assert total == 2
        assert moved == 1
        assert failed == 1
        assert success is False
        assert (tmp_path / "Images" / "good.jpg").exists()
    finally:
        # Restore permissions so tmp_path cleanup doesn't fail
        music_dir.chmod(0o700)


# --- New tests for preview() ---


def test_preview_lists_files_without_moving(tmp_path):
    file = tmp_path / "photo.jpg"
    file.write_text("image")

    result, success = preview(str(tmp_path))

    assert success is True
    assert result == [("photo.jpg", tmp_path / "Images")]
    # preview should not actually move anything
    assert file.exists()


def test_preview_empty_directory(tmp_path):
    result, success = preview(str(tmp_path))

    assert success is True
    assert result == []


def test_preview_nonexistent_path_returns_empty_and_failure(tmp_path):
    missing = tmp_path / "does_not_exist"

    result, success = preview(str(missing))

    assert result == []
    assert success is False


def test_preview_path_is_a_file_not_a_directory_returns_failure(tmp_path):
    file_path = tmp_path / "not_a_folder.txt"
    file_path.write_text("i am a file")

    result, success = preview(str(file_path))

    assert result == []
    assert success is False
