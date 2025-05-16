export default function Button({ disabled, children, onClick, varient }) {
    return <span
        onClick={onClick}
        className={`flex justify-center rounded-md text-xl max-w-72 cursor-pointer text-white px-24 py-3 ${disabled ? "bg-blue-400" : "bg-teal-400"}`}>
        {children}
    </span>;
}