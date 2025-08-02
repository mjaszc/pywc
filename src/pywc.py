from pathlib import Path
import os
import click


@click.command()
@click.option("-c", "count_bytes", is_flag=True, help="Byte count of the file")
@click.option("-l", "count_lines", is_flag=True, help="Line count in the file")
@click.option("-w", "count_words", is_flag=True, help="Words count in the file")
@click.option("-m", "count_chars", is_flag=True, help="Character count in the file")
@click.argument("filepath", type=click.Path(exists=True))
def cli(
    count_bytes,
    count_lines,
    count_words,
    count_chars,
    filepath,
):
    if count_bytes:
        byte_count = os.path.getsize(Path(filepath))
        click.echo(f"{byte_count} {filepath}")

    if count_lines:
        line_count = sum(1 for _ in open(filepath))
        click.echo(f"{line_count} {filepath}")

    if count_words:
        with open(filepath) as f:
            s = f.read()
            word_list = s.split()
            word_count = len(word_list)
            click.echo(f"{word_count} {filepath}")

    if count_chars:
        with open(filepath, "rb") as f:
            s = f.read()
            char_count = len(s.decode("utf-8"))
            click.echo(f"{char_count} {filepath}")


if __name__ == "__main__":
    cli()
