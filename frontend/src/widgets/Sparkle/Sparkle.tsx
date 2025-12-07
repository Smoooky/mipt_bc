import './Sparkle.css'

type SparkleProps = {
    size?: number,
    color?: string,
    duration?: number, // в секундах
    x?: string,
    y?: string,
}

const Sparkle = ({ size = 2, color = '255,255,255', duration = 1.5, x = '0', y = '0' }: SparkleProps) => {
    return (
        <div
            className={`sparkle-shadow rounded-full relative`}
            style={{
                '--sparkle-size': `${size}px`,
                '--sparkle-blur-start': '0px',
                '--sparkle-blur-mid': `${size/2}px`,
                '--sparkle-spread': `${size}px`,
                '--sparkle-color': `${color}`,
                '--sparkle-duration': `${duration}s`,
                top: y,
                left: x,
            } as React.CSSProperties}
        />
    )
}

export default Sparkle