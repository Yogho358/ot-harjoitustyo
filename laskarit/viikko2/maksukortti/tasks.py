from invoke import task

@task
def test(ctx):
    ctx.run("pytest src")

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("puthon3 src/index.py")