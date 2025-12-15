const Values = () => {
    return (
        <div className="w-full box-border pt-20 pb-20 pr-3 pl-3 bg-bg-dark flex justify-center">
            <div className="w-full max-w-[1200px] flex flex-col gap-20 justify-center items-center">
                <div className="flex flex-col gap-6 items-center w-full">
                    <span className="text-[0.9rem] text-accent-light font-bold">
                        НАШИ ЦЕННОСТИ
                    </span>
                    <span className="text-5xl font-bold text-text-second">
                        Что нас <span className="accent-gradient-text">объединяет</span>
                    </span>
                    <span className="text-[1.1rem] text-text-third text-center">
                        Мы верим, что успех строится на фундаменте сильных ценностей и общих целей
                    </span>
                </div>
                <div className="grid grid-cols-4 justify-between gap-8 max-w-6xl mx-auto w-full">
                    <div className="group flex flex-col gap-3 items-start rounded-xl bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                        <div className="aspect-square w-14 rounded-xl bg-accent-darker flex justify-center items-center mb-1 transition-transform duration-200 group-hover:scale-110">
                            <span className="text-3xl text-accent-light leading-0">
                                О
                            </span>
                        </div>
                        <span className="text-[1.4rem] font-bold text-text-second">
                            Амбициозность
                        </span>
                        <span className="text-[1rem] text-text-third">
                            Ставим высокие цели и достигаем их вместе с единомышленниками
                        </span>
                    </div>
                    <div className="group flex flex-col gap-3 items-start rounded-xl bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                        <div className="aspect-square w-14 rounded-xl bg-accent-darker flex justify-center items-center mb-1 transition-transform duration-200 group-hover:scale-110">
                            <span className="text-3xl text-accent-light leading-0">
                                ?
                            </span>
                        </div>
                        <span className="text-[1.4rem] font-bold text-text-second">
                            Инновации
                        </span>
                        <span className="text-[1rem] text-text-third">
                            Внедряем передовые технологии и подходы в бизнес-процессы
                        </span>
                    </div>
                    <div className="group flex flex-col gap-3 items-start rounded-xl bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                        <div className="aspect-square w-14 rounded-xl bg-accent-darker flex justify-center items-center mb-1 transition-transform duration-200 group-hover:scale-110">
                            <span className="text-3xl text-accent-light leading-0">
                                PT
                            </span>
                        </div>
                        <span className="text-[1.4rem] font-bold text-text-second">
                            Нетворкинг
                        </span>
                        <span className="text-[1rem] text-text-third">
                            Создаем ценные связи между студентами, менторами и инвесторами
                        </span>
                    </div>
                    <div className="group flex flex-col gap-3 items-start justify-start rounded-xl bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                        <div className="aspect-square w-14 rounded-xl bg-accent-darker flex justify-center items-center mb-1 transition-transform duration-200 group-hover:scale-110">
                            <span className="text-3xl text-accent-light leading-0">
                                W
                            </span>
                        </div>
                        <span className="text-[1.4rem] font-bold text-text-second">
                            Развитие
                        </span>
                        <span className="text-[1rem] text-text-third">
                            Постоянно учимся и развиваем предпринимательские навыки
                        </span>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Values