const Joining = () => {
    return (
        <div className="w-full box-border pt-20 pb-20 pr-3 pl-3 bg-bg-dark flex justify-center">
            <div className="w-full max-w-[1200px] flex">
                <div className="w-1/2 flex flex-col gap-8 items-start">
                    <div className="flex flex-col gap-2">
                        <span className="text-[0.9rem] text-accent-light font-bold">
                            КАК ПОПАСТЬ
                        </span>
                        <span className="text-6xl text-text-second font-bold">
                            Стань частью <span className="accent-gradient-text">сообщества</span>
                        </span>
                    </div>
                    <div className="flex flex-col gap-6 w-full">
                        <div className="flex items-center w-full gap-4">
                            <div className="aspect-square min-w-[60px] rounded-xl accent-gradient-only flex justify-center items-center">
                                <span className="text-text-thirst text-2xl font-bold">
                                    01
                                </span>
                            </div>
                            <div className="flex flex-col gap-2 justify-between">
                                <span className="text-text-second text-[1.2rem] font-bold">
                                    Заполни анкету
                                </span>
                                <span className="text-[1rem] text-text-third">
                                    Расскажи о себе, своих интересах и опыте в бизнесе
                                </span>
                            </div>
                        </div>
                        <div className="flex items-center w-full gap-4">
                            <div className="aspect-square min-w-[60px] rounded-xl accent-gradient-only flex justify-center items-center">
                                <span className="text-text-thirst text-2xl font-bold">
                                    02
                                </span>
                            </div>
                            <div className="flex flex-col gap-2 justify-between">
                                <span className="text-text-second text-[1.2rem] font-bold">
                                    Пройди собеседование
                                </span>
                                <span className="text-[1rem] text-text-third">
                                    Познакомимся лично и обсудим твои цели
                                </span>
                            </div>
                        </div>
                        <div className="flex items-center w-full gap-4">
                            <div className="aspect-square min-w-[60px] rounded-xl accent-gradient-only flex justify-center items-center">
                                <span className="text-text-thirst text-2xl font-bold">
                                    03
                                </span>
                            </div>
                            <div className="flex flex-col gap-2 justify-between">
                                <span className="text-text-second text-[1.2rem] font-bold">
                                    Присоединяйся
                                </span>
                                <span className="text-[1rem] text-text-third">
                                    Стань частью сообщества и начни развиваться
                                </span>
                            </div>
                        </div>
                    </div>
                    <button className="cursor-pointer pt-3 pb-3 pr-10 pl-10 rounded-xl accent-gradient transition-all duration-200 hover:-translate-y-[0.125em]">
                        <span className="inline text-[1.2rem] font-bold">
                            {'Подать заявку ->'}
                        </span>
                    </button>
                </div>
                <div className="w-1/2 h-full">
                    <div className="w-full h-full rounded-2xl bg-bg-element-dark flex flex-col gap-6 box-border p-10">
                        <span className="text-[1.6rem] text-text-second font-bold">
                            Что ты получишь
                        </span>
                        <div className="flex flex-col gap-2">
                            <div className="flex gap-4 items-center">
                                <span className="text-2xl text-accent-lightest">O</span>
                                <span className="text-[1.05rem] text-text-second">Доступ ко всем мероприятиям клуба</span>
                            </div>
                            <div className="flex gap-4 items-center">
                                <span className="text-2xl text-accent-lightest">O</span>
                                <span className="text-[1.05rem] text-text-second">Персональный ментор</span>
                            </div>
                            <div className="flex gap-4 items-center">
                                <span className="text-2xl text-accent-lightest">O</span>
                                <span className="text-[1.05rem] text-text-second">Нетворкинг с 500+ участниками</span>
                            </div>
                            <div className="flex gap-4 items-center">
                                <span className="text-2xl text-accent-lightest">O</span>
                                <span className="text-[1.05rem] text-text-second">Помощь в запуске стартапа</span>
                            </div>
                            <div className="flex gap-4 items-center">
                                <span className="text-2xl text-accent-lightest">O</span>
                                <span className="text-[1.05rem] text-text-second">Доступ к инвесторам</span>
                            </div>
                            <div className="flex gap-4 items-center">
                                <span className="text-2xl text-accent-lightest">O</span>
                                <span className="text-[1.05rem] text-text-second">Образовательные программы</span>
                            </div>
                        </div>
                        <div className="w-full box-border p-4 bg-bg-element-blue rounded-xl border border-accent-darker">
                            <span className="text-[0.95rem] text-text-third">
                                <span className="text-accent-light font-bold">Бесплатно</span> для студентов и выпускников МФТИ. Набор открыт круглый год.
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Joining