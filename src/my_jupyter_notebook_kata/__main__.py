"""Main entry point."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """My Python Jupyter/AI sandbox Sandbox."""
    print("My Python Jupyter/AI Sandbox is ready.")


if __name__ == "__main__":
    main(prog_name="my-kata")  # pragma: no cover
