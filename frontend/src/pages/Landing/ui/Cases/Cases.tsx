const Cases = () => {
    return (
         <div className="w-full box-border pt-20 pb-20 pr-3 pl-3 bg-bg-light-grey flex justify-center">
            <div className="w-full max-w-[1200px] flex flex-col gap-20 justify-center items-center">
                <div className="flex flex-col gap-6 items-center w-full">
                    <span className="text-[0.9rem] text-accent-light font-bold">
                        УСПЕШНЫЕ ПРОЕКТЫ
                    </span>
                    <span className="text-5xl font-bold text-text-second">
                        Кейсы наших <span className="accent-gradient-text">выпускников</span>
                    </span>
                    <span className="text-[1.1rem] text-text-third text-center">
                        Стартапы, которые начались в нашем клубе и стали успешными бизнесами
                    </span>
                </div>
                <div className="w-full grid grid-cols-3 max-w-6xl gap-8">
                    <div className="flex flex-col rounded-2xl bg-bg-element-dark border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow overflow-hidden">
                        <div className="w-full h-30 blue-gradient box-border pt-6 pb-6 pl-6 pr-6 justify-start items-end flex">
                            <span className="box-border pt-1 pb-1 pr-3 pl-3 text-[0.7rem] text-text-second bg-[#29303d57] rounded-2xl">
                                EdTech
                            </span>
                        </div>
                        <div className="box-border pt-6 pb-6 pl-6 pr-6 flex flex-col gap-4 items-start">
                            <span className="text-2xl text-text-second font-bold">
                                TechFlow
                            </span>
                            <span className="text-[1.05rem] text-text-third">
                                Платформа для автоматизации образовательных процессов. Привлекли $500K инвестиций.
                            </span>
                            <div className="w-full">
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        $500K инвестиций
                                    </span>
                                </div>
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        10K+ пользователей
                                    </span>
                                </div>
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        3 страны
                                    </span>
                                </div>
                            </div>
                            <button className="box-border pt-1 pb-1 pr-4 pl-4 rounded-xl bg-none transition-colors duration-200 hover:bg-bg-grey-transparent cursor-pointer flex gap-3 group relative">
                                <span className="text-[0.95rem] text-text-second font-bold">
                                    Подробнее
                                </span>
                                <span className="text-text-third text-[1rem] font-bold relative left-0 transition-all duration-200 group-hover:left-1">
                                    OP
                                </span>
                            </button>
                        </div>
                    </div>
                    <div className="flex flex-col rounded-2xl bg-bg-element-dark border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow overflow-hidden">
                        <div className="w-full h-30 green-gradient box-border pt-6 pb-6 pl-6 pr-6 justify-start items-end flex">
                            <span className="box-border pt-1 pb-1 pr-3 pl-3 text-[0.7rem] text-text-second bg-[#29303d57] rounded-2xl">
                                CleanTech
                            </span>
                        </div>
                        <div className="box-border pt-6 pb-6 pl-6 pr-6 flex flex-col gap-4 items-start">
                            <span className="text-2xl text-text-second font-bold">
                                GreenEnergy
                            </span>
                            <span className="text-[1.05rem] text-text-third">
                                Решения для мониторинга и оптимизации энергопотребления в промышленности.
                            </span>
                            <div className="w-full">
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        $1M оборот
                                    </span>
                                </div>
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        50+ клиентов
                                    </span>
                                </div>
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        Резидент Сколково
                                    </span>
                                </div>
                            </div>
                            <button className="box-border pt-1 pb-1 pr-4 pl-4 rounded-xl bg-none transition-colors duration-200 hover:bg-bg-grey-transparent cursor-pointer flex gap-3 group relative">
                                <span className="text-[0.95rem] text-text-second font-bold">
                                    Подробнее
                                </span>
                                <span className="text-text-third text-[1rem] font-bold relative left-0 transition-all duration-200 group-hover:left-1">
                                    OP
                                </span>
                            </button>
                        </div>
                    </div>
                    <div className="flex flex-col rounded-2xl bg-bg-element-dark border border-border-dark-grey transition-transform duration-300 hover:-translate-y-2 element-shadow overflow-hidden">
                        <div className="w-full h-30 pink-gradient box-border pt-6 pb-6 pl-6 pr-6 justify-start items-end flex">
                            <span className="box-border pt-1 pb-1 pr-3 pl-3 text-[0.7rem] text-text-second bg-[#29303d57] rounded-2xl">
                                AI/ML
                            </span>
                        </div>
                        <div className="box-border pt-6 pb-6 pl-6 pr-6 flex flex-col gap-4 items-start">
                            <span className="text-2xl text-text-second font-bold">
                                DataMind
                            </span>
                            <span className="text-[1.05rem] text-text-third">
                                AI-сервис для анализа бизнес-данных и прогнозирования продаж.
                            </span>
                            <div className="w-full">
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        Y Combinator
                                    </span>
                                </div>
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        100K ARR
                                    </span>
                                </div>
                                <div className="box-border pt-0.5 pb-0.5 pr-3 pl-3 bg-bg-element-blue float-left rounded-xl mb-2 mr-2">
                                    <span className="text-[0.8rem] text-accent-light">
                                        Топ-10 ProductHunt
                                    </span>
                                </div>
                            </div>
                            <button className="box-border pt-1 pb-1 pr-4 pl-4 rounded-xl bg-none transition-colors duration-200 hover:bg-bg-grey-transparent cursor-pointer flex gap-3 group relative">
                                <span className="text-[0.95rem] text-text-second font-bold">
                                    Подробнее
                                </span>
                                <span className="text-text-third text-[1rem] font-bold relative left-0 transition-all duration-200 group-hover:left-1">
                                    OP
                                </span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Cases