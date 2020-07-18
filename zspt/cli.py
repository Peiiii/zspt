import fire
class Cli:
    def hi(self):
        s='Hi! This is wkweb, simple yet powerful!'.center(50,'*')
        print(s)

def main():
    cli=Cli()
    fire.Fire(cli)

if __name__ == '__main__':
    main()
