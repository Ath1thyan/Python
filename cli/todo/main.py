import click

@click.group()
def cli():
    pass

@click.command()
@click.option("--name", prompt="Enter your name", help="Name of the user")
def hello(name):
    click.echo(f'Hello, {name}!')

PRIORITIES = {
    "o": "Optional",
    "h": "High",
    "m": "Medium",
    "l": "Low",
    "n": "None",
    "c": "Crucial"
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Enter the todo name", help="Name of the todo item")
@click.option("-d", "--desc", prompt="Describe the todo", help="Description of the todo item")
def add_todo(name, desc, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {desc} [Priority: {PRIORITIES[priority]}]")
        f.write("\n")

@click.command()
@click.argument("idx", type=int, required=1)
def delete_todo(idx):
    with open("mytodos.txt", "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodos.txt", "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            print(f"{idx}: {todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"{idx}: {todo}")

cli.add_command(hello)
cli.add_command(add_todo)
cli.add_command(delete_todo)
cli.add_command(list_todos)

if __name__ == '__main__':
    cli()