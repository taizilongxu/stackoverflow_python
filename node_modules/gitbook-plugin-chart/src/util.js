let _uuidCounter = 0;
export function uuid() {
    return `plugin-chart-${++_uuidCounter}`;
};