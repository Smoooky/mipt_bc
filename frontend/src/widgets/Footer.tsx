const Footer = () => {
  return (
    <div className="w-full box-border pt-20 pb-20 pr-3 pl-3 bg-bg-dark border-t border-t-border-dark flex justify-center">
      <div className="max-w-[1200px] w-full">
        <div className="flex flex-col gap-10">
          <div className="flex gap-45 items-start">
          <div className="flex flex-col gap-4">
            <div className="flex gap-4 items-center">
              <div className="p-2 box-border accent-gradient aspect-square flex justify-center items-center rounded-xl">
                <span className="text-2xl font-bold">БК</span>
              </div>
              <span className="text-[1.2rem] text-text-second font-bold">
                Бизнес Клуб МФТИ
              </span>
            </div>
            <span className="text-[1rem] text-text-third max-w-115">
              Объединяем талантливых людей для создания инновационного бизнеса и развития предпринимательской культуры в МФТИ.
            </span>
          </div>
          <div className="flex flex-col gap-4 items-start">
            <span className="text-[1rem] text-text-second font-bold">
              Клуб
            </span>
            <button className="cursor-pointer">
              <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                О клубе
              </span>
            </button>
            <button className="cursor-pointer">
              <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                Мероприятия
              </span>
            </button>
            <button className="cursor-pointer">
              <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                Активности
              </span>
            </button>
            <button className="cursor-pointer">
              <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                Кейсы
              </span>
            </button>
          </div>
          <div className="flex flex-col gap-4 items-start">
            <span className="text-[1rem] text-text-second font-bold">
              Ресурсы
            </span>
            <button className="cursor-pointer">
              <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                База знаний
              </span>
            </button>
            <button className="cursor-pointer">
              <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                Менторы
              </span>
            </button>
            <button className="cursor-pointer">
              <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                FAQ
              </span>
            </button>
            <button className="cursor-pointer">
              <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                Контакты
              </span>
            </button>
          </div>
          </div>
          <div className="flex justify-between box-border pt-8 border-t border-t-border-dark">
            <span className="text-[0.9rem] text-text-third">
              © 2024 Бизнес Клуб МФТИ. Все права защищены.
            </span>
            <div className="flex gap-5">
              <button className="cursor-pointer">
                <span className="text-[0.9rem] text-text-third transition-colors duration-200 hover:text-text-second">
                  Политика конфиденциальности
                </span>
              </button>
              <button className="cursor-pointer">
                <span className="text-[0.9rem] text-text-third transition-colors duration-200 hover:text-text-second">
                  Пользовательское соглашение
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
};

export default Footer;
