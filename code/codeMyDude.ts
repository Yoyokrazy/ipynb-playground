/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

// @ts-nocheck

import { Disposable } from 'vs/base/common/lifecycle';
import 'vs/css!./stickyScroll';
import { ICodeEditor, IOverlayWidget } from 'vs/editor/browser/editorBrowser';
import { fib } from './fibonacci_utils';

interface a {

}

const other = 55;

interface b {

} woah



export class StickyScrollWidget extends Disposable implements IOverlayWidget {

	// this is a comment. woah.

	constructor(
		private readonly _editor?: ICodeEditor
	) {
		super();
		this._layoutInfo = this._editor.getLayoutInfo();
		this._rootDomNode = document.createElement('div');
		this._rootDomNode.className = 'sticky-widget';
		function StickyScrollBehaviorShowerFunctionThing() {
			for (const i = 0; i < this._editor.getModel()!.getLineCount(); i++) {
				console.log(i);
				console.log(i);
				console.log(i);
				console.log(i);
			}

		}
	}

    

	private something() {
		asdfasdf
		asdfa
		SVGAnimatedTransformListdf
	}
}

const thingy = new StickyScrollWidget();


async (params:type) => {

}

class {

	// comment!

}

fib(2)

export interface something {

}

export class MultiDocumentHighlight {

	/**
	 * The URI of the document containing the highlights.
	 */
	uri: Uri;

	/**
	 * The highlights for the document.
	 */
	highlights: DocumentHighlight[];

	/**
	 * Creates a new instance of MultiDocumentHighlight.
	 * @param uri The URI of the document containing the highlights.
	 * @param highlights The highlights for the document.
	 */
	constructor(uri: Uri, highlights: DocumentHighlight[]);
}

interface MultiDocumentHighlight {
	/**
	 * The URI of the document that the highlights belong to.
	 */
	uri: UriComponents;

	/**
	 * The set of highlights for the document.
	 */
	highlights: DocumentHighlight[];
}
