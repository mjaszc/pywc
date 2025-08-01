from pathlib import Path
import os
import click


@click.command()
@click.option(
    "-c", "count_bytes", is_flag=True, help="Print the byte count of the file"
)
@click.option(
    "-l", "count_lines", is_flag=True, help="Print the number of lines in the file"
)
@click.argument("filepath", type=click.Path(exists=True))
def cli(
    count_lines,
    count_bytes,
    filepath,
):
    if count_lines:
        line_count = sum(1 for _ in open(filepath))
        click.echo(f"{line_count} {filepath}")

    if count_bytes:
        byte_count = os.path.getsize(Path(filepath))
        click.echo(f"{byte_count} {filepath}")


if __name__ == "__main__":
    cli()
