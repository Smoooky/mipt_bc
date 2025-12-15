const Activities = () => {
    return (
        <div className="w-full bg-bg-dark box-border pt-20 pb-20 pr-3 pl-3 flex justify-center">
            <div className="w-full max-w-[1200px] flex flex-col gap-20 justify-center items-center">
                <div className="flex flex-col gap-6 items-center w-full">
                    <span className="text-[0.9rem] text-accent-light font-bold">
                        АКТИВНОСТИ
                    </span>
                    <span className="text-5xl font-bold text-text-second">
                        Чем мы <span className="accent-gradient-text">занимаемся</span>
                    </span>
                    <span className="text-[1.1rem] text-text-third text-center">
                        Разнообразные форматы для развития бизнес-навыков и запуска собственных проектов
                    </span>
                </div>
                <div className="flex flex-col gap-6 w-full">
                    <div className="w-full grid grid-cols-3 gap-6">
                        <div className="group rounded-xl flex flex-col gap-3 bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                            <div className="flex items-center gap-4">
                                <div className="aspect-square w-[50px] bg-bg-element-blue rounded-xl flex justify-center items-center transition-colors duration-200 group-hover:bg-accent-darker">
                                    <span className="text-3xl text-accent-light">
                                        Y
                                    </span>
                                </div>
                                <span className="text-[1.1rem] font-bold text-text-second">
                                    Питч-сессии
                                </span>
                            </div>
                            <span className="text-[1.05rem] text-text-third">
                                Регулярные презентации проектов перед экспертами и инвесторами
                            </span>
                        </div>
                        <div className="group rounded-xl flex flex-col gap-3 bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                            <div className="flex items-center gap-4">
                                <div className="aspect-square h-full w-[50px] bg-bg-element-blue rounded-xl flex justify-center items-center transition-colors duration-200 group-hover:bg-accent-darker">
                                    <span className="text-3xl text-accent-light">
                                        JP
                                    </span>
                                </div>
                                <span className="text-[1.1rem] font-bold text-text-second">
                                    Образовательные программы
                                </span>
                            </div>
                            <span className="text-[1.05rem] text-text-third">
                                Курсы и мастер-классы от практикующих предпринимателей
                            </span>
                        </div>
                        <div className="group rounded-xl flex flex-col gap-3 bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                            <div className="flex items-center gap-4">
                                <div className="aspect-square w-[50px] bg-bg-element-blue rounded-xl flex justify-center items-center transition-colors duration-200 group-hover:bg-accent-darker">
                                    <span className="text-3xl text-accent-light">
                                        OI
                                    </span>
                                </div>
                                <span className="text-[1.1rem] font-bold text-text-second">
                                    Менторство
                                </span>
                            </div>
                            <span className="text-[1.05rem] text-text-third">
                                Персональное наставничество от опытных бизнесменов
                            </span>
                        </div>
                    </div>
                    <div className="w-full grid grid-cols-3 gap-6">
                        <div className="group rounded-xl flex flex-col gap-3 bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                            <div className="flex items-center gap-4">
                                <div className="aspect-square w-[50px] bg-bg-element-blue rounded-xl flex justify-center items-center transition-colors duration-200 group-hover:bg-accent-darker">
                                    <span className="text-3xl text-accent-light">
                                        D
                                    </span>
                                </div>
                                <span className="text-[1.1rem] font-bold text-text-second">
                                    Нетворкинг
                                </span>
                            </div>
                            <span className="text-[1.05rem] text-text-third">
                                Неформальные встречи для обмена опытом и идеями
                            </span>
                        </div>
                        <div className="group rounded-xl flex flex-col gap-3 bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                            <div className="flex items-center gap-4">
                                <div className="aspect-square h-full w-[50px] bg-bg-element-blue rounded-xl flex justify-center items-center transition-colors duration-200 group-hover:bg-accent-darker">
                                    <span className="text-3xl text-accent-light">
                                        {`<>`}
                                    </span>
                                </div>
                                <span className="text-[1.1rem] font-bold text-text-second">
                                    Хакатоны
                                </span>
                            </div>
                            <span className="text-[1.05rem] text-text-third">
                                Интенсивные сессии разработки продуктов и прототипов
                            </span>
                        </div>
                        <div className="group rounded-xl flex flex-col gap-3 bg-bg-element-dark box-border pt-6 pb-6 pl-6 pr-6 border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow">
                            <div className="flex items-center gap-4">
                                <div className="aspect-square w-[50px] bg-bg-element-blue rounded-xl flex justify-center items-center transition-colors duration-200 group-hover:bg-accent-darker">
                                    <span className="text-3xl text-accent-light">
                                        X
                                    </span>
                                </div>
                                <span className="text-[1.1rem] font-bold text-text-second">
                                    Конкурсы
                                </span>
                            </div>
                            <span className="text-[1.05rem] text-text-third">
                                Соревнования стартапов с призами и грантами
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Activities