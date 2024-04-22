from Menu import Menu


def main():
    try:
        print("Iniciando programa...")
        m = Menu("Trenes S.A")
        m.mainloop()
        print("Cerrando programa...")
    except Exception as e:
        print(f"Ha ocurrido la excepcion: {e}, cerrando programa.")


if __name__ == "__main__":
    main()
