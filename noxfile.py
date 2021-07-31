import tempfile

from nox_poetry import session


@session(python="3.8")
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@session(python=["3.8", "3.9"])
def tests(session):
    session.install("pytest", ".")
    session.run("pytest", *session.posargs)
