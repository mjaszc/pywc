from pathlib import Path
import os
import click
import sys


@click.command()
@click.option("-c", "count_bytes", is_flag=True, help="Byte count of the file")
@click.option("-l", "count_lines", is_flag=True, help="Line count in the file")
@click.option("-w", "count_words", is_flag=True, help="Words count in the file")
@click.option("-m", "count_chars", is_flag=True, help="Character count in the file")
@click.argument("filepath", required=False, type=click.Path(exists=True))
def cli(
    count_bytes,
    count_lines,
    count_words,
    count_chars,
    filepath,
):
    if filepath == None:
        content = sys.stdin.read()

        byte_content = content.encode("utf-8")
        byte_count = len(byte_content)
        line_count = content.count("\n")
        word_count = len(content.split())

        if count_bytes:
            click.echo(f"{byte_count}")
        elif count_lines:
            click.echo(f"{line_count}")
        elif count_words:
            click.echo(f"{word_count}")
        elif count_chars:
            char_count = len(byte_content.decode("utf-8"))
            click.echo(f"{char_count}")
        else:
            click.echo(f"{byte_count} {word_count} {line_count}")
    else:
        byte_count = os.path.getsize(Path(filepath))
        line_count = sum(1 for _ in open(filepath))
        word_count = 0

        if count_bytes:
            click.echo(f"{byte_count} {filepath}")
        elif count_lines:
            click.echo(f"{line_count} {filepath}")
        elif count_words:
            with open(filepath) as f:
                s = f.read()
                word_count = len(s.split())
                click.echo(f"{word_count} {filepath}")
        elif count_chars:
            with open(filepath, "rb") as f:
                s = f.read()
                char_count = len(s.decode("utf-8"))
                click.echo(f"{char_count} {filepath}")
        else:
            with open(filepath) as f:
                s = f.read()
                word_count = len(s.split())
            click.echo(f"{byte_count} {word_count} {line_count} {filepath}")


if __name__ == "__main__":
    cli()
