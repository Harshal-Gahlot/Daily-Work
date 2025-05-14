export default function Button({ disabled, children, onClick }) {
    return <span onClick={onClick} className={`flex justify-center rounded-md text-xl max-w-72 cursor-pointer text-white py-3 ${disabled ? "bg-blue-400" : "bg-teal-400"}`}>
        {children}
    </span>;
}