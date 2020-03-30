(function(exports) {

    'use strict';

    function PinterestGrid(options) {
        this.settings = Object.assign({
            delay: 100,
            shorterFirst: true,
            gutter: 6
        }, options);
        this.loaded = false;
        this.transform = _getTransformProperty();

        // Objetos del DOM
        this.$container = (options.container instanceof Node)
            ? options.container
            : document.querySelector(options.container);
        if (!this.$container) return false;

        this.$itemCollection = (options.item instanceof NodeList)
            ? options.item
            : this.$container.querySelectorAll(options.item);
        if (!this.$itemCollection || this.$itemCollection.length === 0) return false;

        if (!this.loaded) {
            return this.init();
        }
    }

    PinterestGrid.prototype.init = function() {
        this.loaded = true;
        this.$container.style.width = '';

        var gutter = parseInt(this.settings.gutter);
        var containerWidth = this.$container.getBoundingClientRect().width;
        var itemsWidth = this.$itemCollection[0].getBoundingClientRect().width + gutter;
        var cols = Math.max(Math.floor((containerWidth - gutter) / itemsWidth), 1);

        containerWidth = (itemsWidth * cols + gutter) + 'px';
        this.$container.style.width = containerWidth;
        this.$container.style.position = 'relative';

        var itemsPosY = [];
        var itemsPosX = [];

        for (var i = 0; i < cols; i++) {
            itemsPosX.push(i * itemsWidth + gutter);
            itemsPosY.push(gutter);
        }

        Array.from(this.$itemCollection).forEach(function(item, i) {
            var firstItem, itemIndex, posX, posY;

            if (this.settings.shorterFirst) {
                firstItem = itemsPosY.slice(0).sort(function(a, b){ return a - b }).shift();
                itemIndex = itemsPosY.indexOf(firstItem);
            } else {
                itemIndex = i % cols;
            }

            posX = itemsPosX[itemIndex];
            posY = itemsPosY[itemIndex];

            item.style.position = 'absolute';
            item.style.webkitBackfaceVisibility = item.style.backfaceVisibility = 'hidden';
            item.style[this.transform] = 'translate3d(' + posX + 'px, ' + posY + 'px, 0)';

            itemsPosY[itemIndex] += item.getBoundingClientRect().height + gutter;

            if (!/loaded/.test(item.className)) {
                setTimeout(function() {
                    item.classList.add(item.className.split(' ')[0] + '--loaded');
                }, (parseInt(this.settings.delay) * i));
            }

        }.bind(this));

        var containerHeight = itemsPosY.slice(0).sort(function(a, b) { return a - b }).pop();
        this.$container.style.height = containerHeight + 'px';

        if (!/loaded/.test(this.$container.className)) {
            this.$container.classList.add(this.$container.className.split(' ')[0] + '--loaded');
        }

        if (typeof this.settings.callback === 'function') {
            this.settings.callback(this.$itemCollection);
        }
    };

    function _getTransformProperty() {
        var style = document.createElement('div').style;
        var transform;
        var vendorProp;

        if (undefined !== style[vendorProp = 'webkitTransform']) {
            transform = vendorProp;
        }

        if (undefined !== style[vendorProp = 'msTransform']) {
            transform = vendorProp;
        }

        if (undefined !== style[vendorProp = 'transform']) {
            transform = vendorProp;
        }

        return transform;
    }

    // AMD
    if (typeof define === 'function' && define.amd) {
        define(function() {
            return PinterestGrid
        });
    }

    // CommonJS
    else if (typeof module !== 'undefined' && module.exports) {
        module.exports = PinterestGrid;
    }

    // Global
    else {
        exports.PinterestGrid = PinterestGrid;
    }
}(this));