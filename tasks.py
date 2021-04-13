from invoke import task

@task
def test(ctx):
    ctx.run("pytest src")

@task
def start(ctx):
    ctx.run("python3 src/rytmipeli.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task(coverage_report)
def see_coverage_report(ctx):
    ctx.run('firefox htmlcov')
