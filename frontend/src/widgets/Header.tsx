const Header = () => {
  return (
    <>
      <div className="_header w-full fixed flex justify-center z-100 p-4 box-border bg-bg-header-dark rounded-b-2xl border-b-border-dark border-b">
        <div className="max-w-[1200px] flex justify-between w-full">
          <div className="flex items-center gap-4">
            <div className="flex items-center justify-center">
              <div className="p-2 box-border accent-gradient aspect-square flex justify-center items-center rounded-xl">
                <span className="text-2xl font-bold">БК</span>
              </div>
            </div>
            <div className="flex flex-col gap-1 jusify-between">
              <span className="text-text-second text-xl">Бизнес Клуб</span>
              <span className="text-[1rem] text-text-third">МФТИ</span>
            </div>
          </div>
          <div className="flex justify-around items-center gap-5">
            <div className="flex justify-center">
              <button className="cursor-pointer">
                <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                  О клубе
                </span>
              </button>
            </div>
            <div className="flex justify-center items-center">
              <button className="cursor-pointer">
                <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                  Мероприятия
                </span>
              </button>
            </div>
            <div className="flex justify-center items-center">
              <button className="cursor-pointer">
                <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                  Активности
                </span>
              </button>
            </div>
            <div className="flex justify-center items-center">
              <button className="cursor-pointer">
                <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                  Кейсы
                </span>
              </button>
            </div>
            <div className="flex justify-center items-center">
              <button className="cursor-pointer">
                <span className="text-[1rem] text-text-third transition-colors duration-200 hover:text-text-second">
                  Партнеры
                </span>
              </button>
            </div>
          </div>
          <div className="flex items-center">
            <button
              className="cursor-pointer box-border pt-2 pb-2 pr-4 pl-4 accent-gradient accent-gradient-shadow rounded-xl
                        transition-transform duration-200 hover:-translate-y-[0.125em]"
            >
              <span className="text-[1rem] font-bold text-text-thirst">
                Вступить в клуб
              </span>
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default Header;
